if (candles[i-1][:h] > candles[i-2][:h]) and (candles[i-1][:h] > candles[i][:h])
    puts "DownFractal"
end

if (candles[i-1][:l] < candles[i-2][:l]) and (candles[i-1][:l] < candles[i][:l])
    puts "UpFractal"
end
