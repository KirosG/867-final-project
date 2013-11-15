function [result] = multisvmclassify(models, Test)
numClasses = length(models);
result = zeros(size(Test, 1), 1);
for j=1:size(Test,1)
    for k=1:numClasses
        if(svmclassify(models(k),Test(j,:))) 
            break;
        end
    end
    result(j) = k;
end