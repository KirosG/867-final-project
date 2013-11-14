function [stats_matrix] = slide(x, window)
n = length(x);
overlap = window/2;
%x_trans = fftn(data);
num_steps = floor((n - window - 1)/overlap + 1);
disp(num_steps)
stats_matrix = zeros(num_steps, 9);
for i = 1:num_steps,
   start = (i-1)*(overlap) + 1;
   y = x(start:start+window,:);
   y_x = y(:,1);
   y_y = y(:,2);
   y_z = y(:,3);
   stats_y = zeros(1, 9);
   stats_y(1:3) = [mean(y_x) mean(y_y) mean(y_z)];
   stats_y(4:6) = [std(y_x) std(y_y) std(y_z)];
   C1 = cov(y_x, y_y); C2 = cov(y_y, y_z); C3 = cov(y_z, y_x);
   stats_y(7:9) = [ C1(1,2) C2(1,2) C3(1,2)];
   disp(stats_y);
   stats_matrix(i,:)=stats_y;
end
%TODO: include residual stuff in last window with smaller window size
%plot(1:num_steps, power_matrix(:,1), 1:num_steps, power_matrix(:,2), 1:num_steps, power_matrix(:,3));
end
