function [models] = multisvm(Train, Group, ker, opt)
u = unique(Group);
numClasses = length(u);
numClasses
%build models
for k=1:numClasses
    %Vectorized statement that binarizes Group
    %where 1 is the current class and 0 is all other classes
    G1vAll = (Group == u(k));
    models(k) = svmtrain(Train,G1vAll,'kernel_function', ker, 'options', opt);
end
