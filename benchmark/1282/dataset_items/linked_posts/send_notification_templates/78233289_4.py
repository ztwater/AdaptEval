package org.example;

import java.util.*;

public class Main {


    private static String mutableOuterContextString;

    private static void print(String str) {
        System.out.println("  '" + str + "'");
    }

    private static void printStringWithIdentity(String str) {
        System.out.println("  " + stringWithIdentity(str));
    }

    private static String stringWithIdentity(String str) {
        return "'" + str + "' at " + Objects.toIdentityString(str);
    }

    private final static List<String> numberStrings = Collections.unmodifiableList(Arrays.asList("one", "two", "three"));

    // Here, closures will use the 'reference to String' as given
    // by 'str' at 'closure build time'. Each has been given a specific 'str'.
    // At 'closure call time', the closures created will properly print
    // "one", "two", "three".
    // This corresponds to "function returning function" approach in Python.

    public static List<Runnable> one_two_three_as_expected_1() {
        final List<Runnable> funcs = new ArrayList<>();
        numberStrings.forEach(str -> funcs.add(
                () -> print(str)
        ));
        return funcs;
    }

    // This is the same code as above, just more explicit.

    public static List<Runnable> one_two_three_as_expected_2() {
        final List<Runnable> funcs = new ArrayList<>();
        for (final String str : numberStrings) {
            funcs.add(
                    () -> print(str)
            );
        }
        return funcs;
    }

    // This is the same code as above, just even more explicit.
    // The closure is in fact "just a class" created by the compiler.

    private static class RunnableX implements Runnable {

        private final String str;

        public RunnableX(final String str) {
            this.str = str;
        }

        @Override
        public void run() {
            print(str);
        }
    }

    public static List<Runnable> one_two_three_as_expected_3() {
        final List<Runnable> funcs = new ArrayList<>();
        for (final String str : numberStrings) {
            funcs.add(new RunnableX(str));
        }
        return funcs;
    }

    // As in Python, an interaction between "mutable state in an
    // outside context" and closures leads to surprises.
    //
    // Syntactically, there is not much difference between the
    // closure closing over a local/final variable (str) or a
    // mutable variable from the outside context (mutableOuterContextString)
    // but the compiler must create some different code indeed.

    public static List<Runnable> threethreethree_by_accessing_outside_context_1() {
        final List<Runnable> funcs = new ArrayList<>();
        for (final String str : numberStrings) {
            mutableOuterContextString = str;
            funcs.add(
                    () -> printStringWithIdentity(mutableOuterContextString)
            );
        }
        return funcs;
    }


    // This should be the same code as above, just more explicit.
    // The closure is in fact "just a class" created by the compiler.

    private static class RunnableY implements Runnable {

        @Override
        public void run() {
            printStringWithIdentity(mutableOuterContextString);
        }
    }

    public static List<Runnable> threethreethree_by_accessing_outside_context_2() {
        final List<Runnable> funcs = new ArrayList<>();
        for (final String str : numberStrings) {
            mutableOuterContextString = str;
            funcs.add(new RunnableY());
        }
        return funcs;
    }

    // If the try to reproduce the "three three three" effect with a
    // variable in the local context, we get something that will not compile:
    // "Variable used in lambda expression should be final or effectively final"
    // at "System.out.println(curString2)"

    /*
    public static List<Runnable> three_three_three_this_will_not_compile() {
        final List<Runnable> funcs = new ArrayList<>();
        String curString2;
        for (final String str : numberStrings) {
            curString2 = str;
            funcs.add(() -> print(curString2)); // <--- won't compile
        }
        return funcs;
    }
    */

    // Fixing it Python-style
    // Note that we do not even need to declare a local variable inside the build_..() method.
    // Directly using the variable "outerStr" that has been passed-in is good enough.
    // It is not important whether it has been declared "final" or not in the method declaration.

    public static Runnable build_closure_with_its_own_local_variable(final String outerStr) {
        System.out.println("  Creating closure with a local reference for " + stringWithIdentity(outerStr));
        return () -> printStringWithIdentity(outerStr);
    }

    public static List<Runnable> three_three_three_fixed() {
        final List<Runnable> funcs = new ArrayList<>();
        for (final String str : numberStrings) {
            mutableOuterContextString = str;
            funcs.add(build_closure_with_its_own_local_variable(mutableOuterContextString));
        }
        return funcs;
    }

    public static void main(String[] args) {
        System.out.println("Print 'one', 'two', 'three' as expected, take 1");
        one_two_three_as_expected_1().forEach(r -> r.run());
        System.out.println("Print 'one', 'two', 'three' as expected, take 2");
        one_two_three_as_expected_2().forEach(r -> r.run());
        System.out.println("Print 'one', 'two', 'three' as expected, take 3");
        one_two_three_as_expected_3().forEach(r -> r.run());
        System.out.println("Print 'three', 'three', 'three', unexpectedly, take 1");
        threethreethree_by_accessing_outside_context_1().forEach(r -> r.run());
        System.out.println("Print 'three', 'three', 'three', unexpectedly, take 2");
        threethreethree_by_accessing_outside_context_2().forEach(r -> r.run());
        System.out.println("Print 'one', 'two', 'three' again by creating a local variable");
        three_three_three_fixed().forEach(r -> r.run());
    }
}
