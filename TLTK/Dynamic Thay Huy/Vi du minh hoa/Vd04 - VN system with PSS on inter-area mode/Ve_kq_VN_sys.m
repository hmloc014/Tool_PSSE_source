close all
clear all
NSKIP = 8;
Tsample = 0.01; % sec
dat = dlmread('branch_trip.txt','', NSKIP,0);
%% Initial data
t = dat(:,1);
sp = dat(:,2:end);
% Remove dupplicates
[t1,idx] = unique(t);
sp = sp(idx,:);

% idx = min(find(t > 1.01));
%% interpolation
t0  = min(t);
tend = max(t);
Nsample = fix((tend - t0)/Tsample);
tvec = linspace(t0,tend,Nsample);
sp1 = interp1(t1,sp,tvec);
%% Analysis
da = [tvec' sp1];
ringdown(da)