>>> Z().class_meth
<bound method type.class_meth of <class '__main__.Z'>>
>>> Z().class_meth.__self__
<class '__main__.Z'>
>>> Z().class_meth.__self__.__class__
<class 'type'>
