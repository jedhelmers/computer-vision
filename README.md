# computer-vision
## Finding objects within high-noise images.

### _Road Map_
* an image or stream of images is acquired and read in as a function.
* a light gaussian blur should be applied over the image.
* a portion of the image should be grabbed as a filter. Forrier would probably agree that noise is sort of like a repeating function that can be expressed mathematically. I figure snippets like this might be used as a filter.

**Problems:**
  randomly grabbed filters like this could contain highly specific data that would make it completely useless as a filter. Maybe manually select a filter from a large selection of images?
  
* guassian blur again.
* get derivatives of the image to make gradient maps.
* Canny line search these derivaties to find the lines.
* Hough transform these lines into vectors.
* extend vectors a little until they cross one-another to create shapes.
* compare shapes with predefined shapes. Machine learning stuff
  
  
  
