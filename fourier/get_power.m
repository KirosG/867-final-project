
function [powers] = get_power(y)
%takes a transformed data matrix and calculates power
fs = 6.6901e+09;
n = length(y);
f = (0:n-1)*(fs/n);
y_x = y(:,1);
power_x = sum(y_x.*conj(y_x))/n;
disp(power_x);
y_y = y(:, 2);
power_y = sum(y_y.*conj(y_y))/n;
disp(power_y);
y_z = y(:, 3);
power_z = sum(y_z.*conj(y_z))/n;
disp(power_z);
powers = [power_x, power_y, power_z];
end
