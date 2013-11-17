function [ file_output ] = scrape_kaggle_data(kaggle, fileout)
M = kaggle;
samples = unique(M(:, 5), 'rows');
file_output = zeros(1,10);
for i= 1:length(samples),
    id = samples(i, 1);
    submatrix = M(M(:, 5)==id,:);
    stats_matrix = slide(submatrix(:,2:4), submatrix(:,1), 128);
    n_p = size(stats_matrix,1)
    size(stats_matrix)
    prefix = ones(n_p, 1);
    prefix(:,1) = id*prefix(:,1);
    %size(file_output)
    %size(prefix)
    %size(stats_matrix)
    file_output = vertcat(file_output, horzcat(prefix, stats_matrix(2:));
end
%csvwrite(fileout, file_output);

