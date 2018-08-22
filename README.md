# Sign-O-Voice-Substantiation

The core objective of this project is to provide a two-tier authentication platform comprising of signature and voice as the security 
factors for identification of an individual. The programming language employed is Python and concept is to utilize the best of machine 
learning. Implemented the concept of Digital Image Processing for signature feature extraction and used Artificial Neural Network(ANN) 
for the training purpose. Extracted Mel-frequency Ceptral Coefficient(MFCC) for audio features and applied Dynamic Time Warping(DTW) for
comparison of wave and sequence of voices.


A signature may articulate as a behavioral biometric. It is widely used to recognize a person delivering out daily procedures i.e. bank operations, document analysis, electronic funds transfer, and access control, by using his manual signature
There are basically three types of forgeries as:
 1) Random forgery - This can normally be represented by a signature sample. Forger has no information about the signature style and the name of the person. 
2) Simple forgery - This is a signature with the same shape or the legitimate writer’s name. 
3) Skilled forgery - This is signed by a person who has had access to a genuine signature for practice.

Types of Signature Verification:

A signature verification technique which is used to solve this problem can be divided into two classes Online i.e. Dynamic and Off-line i.e. Static
1)	Online i.e. Dynamic Signature Verification Technique:
Online approach uses pressure-based tablets to capture the signature and takes features such as pressure, speed of writing, no of order of the strokes and the pen pressure at each point.
2)	Offline i.e. Static Signature Verification Technique:
Offline signature verification uses less electronic means and uses images captured by scanner or a camera. Offline verification technique uses features of scanned image to verify the signature.


1.4	IMAGE PRE-PROCESSING

Image pre-processing is used to make the image ready to be able to fed to the Neural Network. For this we apply various methods:
a)	Grayscale Transformations:
In this the colored image of the signature is converted to gray image so that signatures done with different pen ink can be compared.
b)	Scaling:
Let H be the height of the input image and W be the width of the inputted image then the image can be converted to a standard height and width say 500*500 to make the comparison easier.
c)	Denoising:
Image gets degraded while capturing or due to difference in illumination and other objects in the environment.
d)	Background Elimination (thresholding):
Thresholding is the most trivial method as it is necessary to remove background noises in order to perform proper comparison.
e)	Thinning:
The goal of thinning is to eliminate the thickness differences of pen by making the image one pixel thick.



5	 NEURAL NETWORK

The simplest definition of a neural network is “A computing system made up of a number of simple, extremely interrelated 
processing elements, which practice information by their dynamic state response to peripheral inputs”. Neural Network is 
made up of layers. Layers consist of a number of interrelated nodes. The main reasons for the widespread usage of neural 
networks (NNs) in pattern recognition are their power and ease of use. A simple approach is to firstly extract a feature 
set representing the signature (details like length, height, duration, etc.), with several samples from different signers. 
The second step is for the NN to learn the relationship between a signature and its class (either “genuine” or “forgery”). 
Once this relationship has been learned, the network can be presented with test signatures that can be classified as belonging
to a particular signer. NNs therefore are highly suited to modeling global aspects of handwritten signatures.
The proposed system uses features such as global features and local features such as slope & slope direction, density of 
thinned image, width to height ratio, skewness.
These features can be used to train the NNs to recognize the signature as of an existing user or not.



6	MFCC (Mel Frequency Cepstral Coefficient)

The extraction of parametric features of an audio signal is a necessary part to make the recognition more efficient. 
MFCC is based on human hearing perceptions which cannot perceive frequencies over 1Khz. MFCC has two types of filter 
which are spaced linearly at low frequency below 1000 Hz and logarithmic spacing above 1000Hz. A subjective pitch is 
present on Mel Frequency Scale to capture important characteristic of phonetic in speech.
To create data base as HMM model first human voice sample is taken, and then Voice Activity Detection (VAD) separate 
actual date from the samples. MFCC is based on the short-term analysis, and thus from each frame a MFCC vector is computed.
In order to extract the coefficients, the speech sample is taken as the input and hamming window is applied to minimize the
discontinuities of a signal. Then DFT will be used to generate the Mel filter bank. According to Mel frequency warping, the
width of the triangular filters varies and so the log total energy in a critical band around the centre frequency is included.
After warping the numbers of coefficients are obtained. Finally, the Inverse Discrete Fourier Transformer is used for the cepstral
coefficients calculation.

7	GAUSSIAN MIXTURE MODEL
A Gaussian Mixture Model (GMM) is a parametric probability density function represented as a weighted sum of Gaussian
component densities. GMMs are commonly used as a parametric model of the probability distribution of continuous measurements 
or features in a biometric system, such as vocal-tract related spectral features in a speaker recognition system. GMM parameters
are estimated from training data using the iterative ExpectationMaximization (EM) algorithm


ALGORITHM FOR SIGNATURE VERIFICATION
1.Capture the image and store in any format
2.Acquire the signature image 
3.Enhance the inputted signature image by pre-processing 
  3.1 Convert original image to grey scale image 
  3.2 Scaling 
  3.3 Noise Reduction 
  3.4 Background Elimination 
  3.5 Thinning 
4.Extract the various features 
5.Apply the feature vector to the neural network for training purpose
6.Capture testing signature and verify
  6.1 If verified
   6.1.1 Proceed with Voice Recognition
  6.2 Else
   6.2.1 Print Access Denied
   6.2.2 Input another test signature

ALGORITHM FOR VOICE RECOGNITION
1.Capture Background noise (for 5 sec) 
2.Display words from Google API and record user’s voice for those words
3.Repeat Step 2 for saving three voice samples of user 
4.Filter the voice samples by subtracting background noise
5.Extract MFCCs for samples and store
6.Input testing voice
7.Match features using GMM 
  7.1 If Voices Match
   7.1.1 Grant Access
  7.2 Else
	 7.2.1 Deny access
8.Open Application

