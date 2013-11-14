function [power_matrix] = slide(x, window)
x_trans = fftn(x);
n = length(x_trans);
overlap = window/2;
%x_trans = fftn(data);
num_steps = floor((n - window - 1)/overlap + 1);
disp(num_steps)
power_matrix = zeros(num_steps, 3);
for i = 1:num_steps,
   start = (i-1)*(overlap) + 1;
   y = x_trans(start:start+window,:);
   power_y = get_power(y);
   disp(power_y);
   power_matrix(i,:)=power_y;
end
%TODO: include residual stuff in last window with smaller window size
%plot(1:num_steps, power_matrix(:,1), 1:num_steps, power_matrix(:,2), 1:num_steps, power_matrix(:,3));
end
