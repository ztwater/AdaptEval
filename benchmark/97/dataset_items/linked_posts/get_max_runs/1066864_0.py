threshold = 7;
d = 10*rand(1,100000);  % Sample data
b = diff([false (d < threshold) false]);
durations = find(b == -1)-find(b == 1);
