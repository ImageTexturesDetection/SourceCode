function func = randomize()

images = [];
filelist = dir('textures/*.png');
rng shuffle;
nb = ceil(rand(1)*4)+1;
rng shuffle;
nb2 = ceil(rand(1)*4)+1;

for j=1:nb
	imgrow = [];
	for i=1:nb2
		rng shuffle;
		fname = filelist(ceil(rand(1)*26)).name;
		fname = ['textures/',fname];
		tmp = imread(fname);
		imgrow = [imgrow tmp];
		disp([fname 'loaded']);
	end
	images = [images;imgrow];
end
	% imshow(images)
	imwrite(images, 'textures.png'); 
	exit
end