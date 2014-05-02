function z = colorize(image, pattern, threshold,color)
close
close all
clc

%% Param
% threshold= 0.88;
bdd = [];
%%
I=imread(pattern);
mapping=getmapping(8,'u2'); 
in=lbp(I,1,8,mapping,'nh');

file = ['patterns/data-base.mat'];
if exist(file, 'file')
    load(file,'-mat','bdd');
end

% if sum(min(in,bdd(end,1))) ==1
%     bdd(end,2)=threshold;
% else
    bdd = [bdd;pattern num2str(threshold)];
% end

file = ['patterns/data-base.mat'];

save(file,'-mat','bdd');

%%
k=image;

im=imread(k);
im2=imread('white.png');
% im1=rgb2gray(im);
im1=im;

h = size(im1,1);
w = size(im1,2);

file = ['data/',image,'.mat'];


load(file,'-mat','point');

%% calcule des similariré
% hold on


% figure('Name',k);
%subplot(1,2,1);
%imshow(im1);
% subplot(1,2,2);
% imshow(im1);

hfig = figure('Visible', 'off');
% imshow(im1, 'Border', 'tight');
% imshow(im2,'InitialMagnification', 'fit', 'Border', 'tight');
imshow(im2,'Border', 'tight');



b = 0 ;% to jump the first rectangle cause it's soo big
for i=2:size(point,1)
    A = im1(point(i,1):point(i,3),point(i,2):point(i,4));
    in1 = lbp(A,1,8,mapping,'nh');
    r = sum(min(in,in1));
    %display(strcat('r=',num2str(rr)));

    % Draw rectangle
    
    if r>threshold  
        hh=point(i,3)-point(i,1);
        ww=point(i,4)-point(i,2);      
        rectangle('position',[point(i,2) point(i,1)  hh ww],'EdgeColor',color/255, 'facecolor',color/255);
        hold on;
    end
end


F = im2frame(zbuffer_cdata(gcf));
imwrite(F.cdata, 'white.png'); 

% hold off
% imwrite(im1,'test.png')
exit
end

function cdata = zbuffer_cdata(hfig)
    % Get CDATA from hardcopy using zbuffer
    % Need to have PaperPositionMode be auto
    orig_mode = get(hfig, 'PaperPositionMode');
    set(hfig, 'PaperPositionMode', 'auto');
    cdata = hardcopy(hfig, '-Dzbuffer', '-r0');
    % Restore figure to original state
    % set(hfig, 'PaperPositionMode', orig_mode);
end