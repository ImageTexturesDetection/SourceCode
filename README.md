##Using de statistical methodes for texture images segmentation

###Betrouni El-Khalil, Melaine Samy, Saliha Aouat 
###Computer science Department
###University of sciences and technology(USTHB), Algiers, Algeria
###{kbetrouni,melaine.samy}@gmail.com ,saouat@usthb.dz


. 0  Abstract:
	This study is an initial attempt to generalize the Texture Segmentation and Matching using LBP Operator method. 
	This thesis first examines the principle of a segmentation and matching algorithm which is to detect a given texture over a given image. 
Then we'll describe our implementation of that automatic detection algorithm that detects all textures in an image with no other information given but the targeted image.
Finally, the method is applied on randomly generated images from a database of over 30 textures.
	On the basis of the results of this research, it can be concluded that texture recognition methods are indeed very powerful and deserve spending more efforts and time on.
. 1  Introduction:
	It is very simple and obvious for us humans to recognize what we see instantly. However, it is not as easy for a computer. The processing performed by the brain being so complex, it is very difficult to analyze, and especially to reproduce them. If we take the example of the textures recognition and segmentation, we find ourselves in the paradox of studying an undefined but perfectly recognizable entity. To recognize a blue sky and distinguish it from a river or the rocks around is basic for the human brain. You can also easily distinguish a plastic table from a wooden one. However, the mere definition of the term "texture" is ambiguous.
So how can we deal with an undefined entity?
	The answer lies in the statistical studies on the different relationships between the pixels that form an image. Researchers have found different formulas and characteristics in order to define and segment textures. Most of the time, the study focuses mainly on the detection of regular patterns forming the texture, by comparing each pixel with the disposition of his entourage.
	Most of the work done in this area so far, aims to recognize a given texture in a certain image. Our job is to propose a generalization of these methods in order to implement it in autonomous systems. They must be able to automatically extract information from a digital image. In other words, they must be able to segment the different textures presented to them. 



The article is organized into five sections. In the next section will be presented the LBP operator and the decomposing architecture used to segment the textures. In the second section we introduce in details the principle of the approach used for the segmentation of textures. The third will be devoted to the presentation of our application as well as tests on randomly generated images.

. 2  Related works :

Local Binary Pattern  :
	This feature was first mentioned by Harwood [Har et al. 93] and was then used by Ojala and Pietikinen [Oja et al. 96 Oja and Pie 99]. The LBP feature has a huge advantage due to its computational simplicity and robustness in the detection of textures. It allows the description of textures according to the local spatial configuration of pixels. 
The principle of calculating the basic LBP (Basic Local Binary Pattern) carried by Ojala [Oja et al. 02] is to compare a pixel at the center with its eight neighbors as shown in the following figure:
Fig.1. Calculation of the LBP operator
	The matrix of FIG I [Fig.1.a] represents the gray level of a pixel at the center and its eight neighbors. The matrix M of the pattern that is shown in figure is calculated as follows: 




Where I (i, j) is the gray level value of the eight neighbors, and gc the gray level of the central pixel (red). The result is assigned in binary format in M (i, j). 
Reading the values of M (i, j) starting from the top left and following a clockwise rotation, the bit pattern m following is obtained: 
m = 10001111 

	This result is then converted to decimal by multiplying each M (i, j) by the corresponding value P (i, j) of the weight matrix [Fig.1.c], the latter is constructed with an ascending power of two, starting from top left and following a clockwise rotation. 
The LBP gray level value of the central pixel in the example is computed as follows: 
				 LBP = 1 + 16 + 32 + 64 + 128 = 241 
The following figure shows the total LBP transformation of an image:
 Original Image					     LBP Image
Fig.2. LBP transform of an image
Ojala [Oja et al. 02] also defined a value of "U" called "transition" equal to the number of transitions from 0 to 1 and 1 to 0 of the value found in the "bit pattern" in Figure [Fig.3].





Fig.3. Extracting the number of transitions from a pattern
	In fact, not all the patterns (256) are useful to describe a texture. According to T. Menp [Men et al. 00], the patterns in which a number of transition U = 2 and U = 0, which are called "uniform patterns" represent the most important information on regular patterns of a texture. Some areas of interest such as corners or edges can be detected by this descriptor. These patterns are also more resistant to geometric transformations such as rotation [Zhe 10]. The use of the following 58 uniform patterns was proposed :













Fig.4. The uniform patterns
	To study the uniformity of a texture, we construct a histogram which is composed of 59 values representing the 58 uniform patterns defined above, plus a final value containing all the "non-uniform patterns."
Fig.5. A texture and its LBP histogram
	Two LBP histograms of two textures are compared as a percentage of similarity. The LBP feature that uses this type of histogram is denoted as LBPu2. This notation means that the LBP is based on the "uniform pattern" having U ≤ 2. Thereafter, LBPu2 will be noted only as LBP.
The decomposing architecture:
	For the image decomposition, we brought our choice on the algorithm of dynamic segmentation [Ham et al segmentation. 13]. It is called this way because it is based on various sizes of segments.
	The algorithm will be applied to an image, having previously texture reference. Its principle is as follows: 
	We start by choosing a point towards which converge the windows of the algorithm. We set a maximum size L of the largest square and generate as many adjacent squares with the same length as possible. Then, we compute the LBP histogram of these squares and their similarities with the texture reference. 

 If the similarity is above the threshold then the square is to be colored, and its position, its size and its histogram are saved. After that, we reduce the size L by distance d and repeat the steps until L becomes smaller than the minimum size of the squares. 
Finally, we color the squares saved.

Advantages of the algorithm: 
	We chose to implement this algorithm in order to propose a solution to generalized research and detection for the several different textures that are present in an image. The dynamic aspect of this algorithm gives it many advantages which include: 
- Squares of different sizes can be extracted and analyzed. 
- Different forms except the squares and different points of convergence can be considered. Therefore, different configurations can be studied. 
- The independence between the proposed architecture and the feature extraction method (LBP in our case) is the main advantage of this approach. This method may therefore be adapted to different use cases. 
The division process is explained in the following figure :





	     (a) First iteration	               (b) Second iteration                    (c) Third iteration





(d) After n number of iterations
Fig.6. Dynamic decomposition architecture using square shaped windows
	The first window that is generated is the main window, other windows adjacent to it and which have the same size are generated. Those that exceed the threshold will then be saved.

. 3  Proposed approach :
	We present in this section our method which presents a generalization that allows the segmentation of an image and the detection of all its textures, having no prior information other than the picture itself.
It is described by the algorithm below:

	In the first place, we simply apply the algorithm on simple images. A white image of the same size as the image to process is generated [Fig.7]. 
This is to be gradually colored and rendered as a final result of the operation. 

The dynamic segmentation algorithm presented above is applied. The return would be a set of squares which will be saved a file. The file will contain the coordinates of the top left corner of each square (x0, y0), its size t and the value of the LBP histogram h. The result will be an array with one element for each square: 
elem = [x0, y0, t, h] 
This file will allow us to not have to repeat this next time the same image will be processed.







Fig.7. The first detection
	We set a size tr for the reference texture that we will chosen from the image. Then we go through the white image from left to right and from top to bottom looking for a blank window of size tr. If a window is found [Fig.7], we generate the LBP histogram of the equivalent window located in the same position in the original image. A color C is set.
	We then go through the squares saved previously and compare their histograms with th the detected reference's histogram. 
There are several methods to calculate the difference between two histograms. We use the method of intersection defined as follows: 
	Let h2 and h2 be two histograms. The comparison value is equal to the sum of minimum frequency of h1 and h2 for each of their elements.


	The more the histograms look the same, the larger the value d gets. Its maximum is 1 if the histograms are identical. 
If the comparison value is above the threshold, the corresponding square in the white image is colored with the color C (C = brown, in the example below). [Fig.8]







Fig.8. Coloring the first detected texture
The search for a new reference is initiated. Search continues for the first white square with the same reference's size tr initially set. The squares similar to the new found reference are colored with the same color C2 [Fig.9] different from C (the first segmented texture color). (green != brown)
Fig.9. Coloring the second detected texture
And we continue until no white square of size tr remains in the white image. The algorithm is then complete. [Fig.10]
Fig.10. Detecting all textures
Controlled Processing: 
	To allow more control over the segmentation and textures recognition, we put in place a learning process feature.
Figure 11. First step
	This will give us the possibility to change each time the threshold of each detected texture and save the satisfactory results of detections of each texture in a database to be used in further proceedings.
Take the example of Figure 11. The first step is identical to the automatic processing.
	A texture is first detected. Note that the threshold used (current threshold = 0.965) is different from the one chosen by default (initial threshold = 0.97). This is because the same texture or a texture resembling highly has been found in the database. The threshold of the latter was therefore chosen.
	We then have the choice to save the threshold in the database, to continue if the result is satisfying, or change it first and then restart the detection of the current texture again. 
	We choose to proceed, until the detection of one of the textures is no longer satisfying. We choose in this case to change the threshold. [Figure 12]
Figure 12. Controlled Porcessing, 3rd iteration
We chose another threshold and apply it.
Figure 12. Controlled Porcessing, 3rd iteration after modification
We will save this threshold in the database so that the next time this value is automatically used. 
The process continues in this manner until all of the image textures are detected [Figure 13].
Figure 13. Controlled Porcessing, Iteration 7
Test images generation:
	Images on which we applied our tests were generated randomly. The textures were extracted from the database Brodatz. 
We used a first algorithm to cut the latter into smaller textures (size 150 * 150px) and put them in a folder Textures.



Then we developed an algorithm that randomly selects textures from the folder previously completed and built the image to be tested.


. 4  Experimentation:
	We will see in more details the results of several tests to see the behavior of the threshold toward different textures.




























	We made a dozen similar tests. We calculated the average threshold per image in the first place, and then, we took into account the coefficients depending on the area they occupy in the image. 
The results are shown in the following graph:








Figure 16. Graph representing avrages
	We notice that, despite the considerable difference between the thresholds of different textures, the average between them remains constant (either counting or not the coefficient on the surface occupied by the textures). This implies that the accuracy in terms of detection remains high.
This figure also indicates that the average values of the thresholds are greater than 95%. 
The error of 5% is due either to the presence of parasites (small parts of other textures) or the limit of accuracy of LBP histograms products.

Additional tests:
in addition to the simple images we used in our study, we tried the algorithme on ceveral other images with more complex shapes, but also in some real satelite pictures.
The results are represented below:





































Figure 18. Satellite Images
. 5  conclusion: 

	We studied the statistical aspects of the characterization and description of textures, and precisely by using the LBP feature that gave us a very powerful tool for texture recognition. 
	We also studied a dynamic segmentation method that can detects and segments a texture in a given image. Our approach was to develop a generalization of that method in order to make an automatic detection of all these textures in a image without any initial information other than the picture itself. The results obtained are very promising and motivating to grant this study more time and more effort. 
	Although some constraints had to be respected, we should know that this work is a first step of applying this method. 


















References

    [Cog 82] J. M Coggins. A Framework for Texture Analysis Based on Spatial Filtering.  PhD thesis, Michigan State University, 1982. 

         [Ham et al. 13]  I. Hamouchene, S. Aouat and H. Lacheheb, New segmentation architecture for texture matching using the LBP method, IEEE Technically, SAI Conference, London UK, October 7-9, 2013.

        [Ham et al. 14] I. Hamouchene, S. Aouat and H. Lacheheb, “Texture Segmentation and Matching Using LBP Operator and GLCM Matrix”, Intelligent Systems for Science and Information, Springer International Publishing, vo. 542, pp. 389-407, 2014.

     [Har et al. 93] D. Harwood, T. Ojala, M. Pietikinen, S. Kelman, S. Davis Texture classification by center-symmetric auto-correlation, using Kullback discrimination of distributions. Technical report, Computer Vision Laboratory, Center for Automation Research, University of Maryland, College Park, Maryland. CAR-TR-678, 1993. 

     [Haw 69] Hawkins, J. K., “Textural Properties for Pattern Recognition,” In Picture Processing and Psychopictorics, B. Lipkin and A. Rosenfeld (editors), Academic Press, New York, 1969. 

     [Maj 09] H.Majdoulayne. Extraction de caractéristiques de texture pour la classification d'images satellites. PhD thesis, université de Toulouse, France, 2009. 

    [Mat and Str 98] A. Materka, M. Strzelecki, Texture Analysis Methods – A Review , Technical University of Lodz, Institute of Electronics, COST B11 report, Brussels 1998

    [Men et al. 00] T. Menp, T. Ojala, M. Pietikinen, M. Soriano , Robust Texture Classification by Subsets of Local Binary Patterns, icpr, vol. 3, pp.3947, 15th International Conference on Pattern  Recognition (ICPR’00) - Volume 3, 2000. 

        [Oja et al. 96] 15. T. Ojala, M. Pietikinen, D.A. Harwood, Comparative Study of Texture Measures with Classification Based on Feature Distributions, Pattern Recognition 19(3):51-59, 1996. 

    [Oja et al. 99] T. Ojala, M. Pietikinen, Unsupervised Texture Segmentation Using Feature Distributions, Pattern Recognition, vol. 32, pp. 477-486, 1999. 

     [Oja et al. 02] T. Ojala , M. Pietikainen  and T. Maenpaa, “Multiresolution gray-scale and rotation invariant texture classiﬁcation with local binary patterns,” PAMI, vol. 24, no. 7, pp. 971–987, 2002. 

      [Ric et al. 74] Richards, W. and A. Polit, “Texture matching,” Kybernetic, 16, pp. 155-162, 1974.

    [Tam et al. 78] Tamura, H., S. Mori, and Y. Yamawaki, “Textural Features Corresponding to Visual Perception,” IEEE Transactions on Systems, Man, and Cybernetics, SMC-8, pp. 460-473, 1978. 

       
 [Zhe 10] Zhenhua Guo Zhang, D. A completed modeling of local binary pattern operator for texture classification. In Image Processing, IEEE Transactions, 2010} 


   [Zuk et al. 81] Zucker, S. W. and K. Kant, “Multiple-level Representations for Texture Discrimination,” In Proceedings of the IEEE Conference on Pattern Recognition and Image Processing, pp. 609-614, Dallas, TX, 1981. 








