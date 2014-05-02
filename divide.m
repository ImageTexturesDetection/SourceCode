function func = divide(image)
close
close all
clc

%% Param
jump     = 10;
limit    = 4;

%%
k=image;

im=imread(k);
% im1=rgb2gray(im);
im1=im;

h = size(im1,1);
w = size(im1,2);

zone = min(h,w);
point = zeros(1,4);

%% constuction de la matrice des zones
% |--------
%|$
%|  \
while zone>=limit
    %display(strcat('Zone : ',int2str(zone)));
    
    zx = fix(h/zone);
    zy = fix(w/zone);
    
    for i=1:zx
        for j=1:zy
            p1_x= (zone*(i-1))+1;
            p1_y= (zone*(j-1))+1;
            
            p2_x= p1_x+zone-1;
            p2_y= p1_y+zone-1;
            
            %display(strcat('=== ',int2str(p1_x),'<=>',int2str(p1_y),'<=>',int2str(p2_x),'<=>',int2str(p2_y)));
            
            point = [point;p1_x p1_y p2_x p2_y];
             
        end
    end
    zone = zone - jump;
end
path = 'data';
if ~exist(path, 'dir')
  mkdir(path);
end
file = ['data/',image,'.mat'];
save(file,'point');

exit
end
