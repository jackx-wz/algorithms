function fact(x)
    if x == 1 then
        return 1
    else
        return x * fact(x - 1)
    end
end

for i=1, 1000000 do
    fact(20)
end
