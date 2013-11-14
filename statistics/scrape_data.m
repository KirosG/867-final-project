function [ file_output ] = scrape_data( filename, fileout )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
M = csvread(filename)
samples = unique(M(:, 1:2), 'rows')
file_output = zeros(1,11);
for i= 1:length(samples),
    id = samples(i, 1);
    activity = samples(i, 2);
    submatrix = M(M(:, 1)==id & M(:,2)==activity,:);
    stats_matrix = slide(submatrix(:,4:6), 128);
    n_p = size(stats_matrix,1)
    size(stats_matrix)
    prefix = ones(n_p, 2);
    prefix(:,1) = id*prefix(:,1);
    prefix(:,2) = activity*prefix(:,2);
    size(file_output)
    size(prefix)
    size(stats_matrix)
    file_output = vertcat(file_output, horzcat(prefix, stats_matrix));
end
csvwrite(fileout, file_output);

