# computer-vision
## Finding objects within high-noise images.

### _Road Map_
1.) an image or stream of images is acquired and read in as a function.

2.) a light gaussian blur should be applied over the image.

3.) a portion of the image should be grabbed as a filter. Forrier would probably agree that noise is sort of like a repeating function that can be expressed mathematically. I figure snippets like this might be used as a filter.

**Problems:**
  randomly grabbed filters like this could contain highly specific data that would make it completely useless as a filter. Maybe manually select a filter from a large selection of images?
  
4.) guassian blur again.

5.) get derivatives of the image to make gradient maps.

6.) Canny line search these derivaties to find the lines.

7.) Hough transform these lines into vectors.

8.) extend vectors a little until they cross one-another to create shapes.

9.) compare shapes with predefined shapes. Machine learning stuff
  
  
  
