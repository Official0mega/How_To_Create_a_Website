#include <iostream>
int main()
{


Learn CSS!


Search
000
Learn CSS
001
Box Model
002
Selectors
003
The cascade
004
Specificity
005
Inheritance
006
Color
007
Sizing Units
008
Layout
009
Flexbox
010
Grid
011
Logical Properties
012
Spacing
013
Pseudo-elements
014
Pseudo-classes
015
Borders
016
Shadows
017
Focus
018
Z-index and stacking contexts
019
Functions
020
Gradients
021
Animations
022
Filters
023
Blend Modes
024
Lists
025
Transitions
026
Overflow
027
Backgrounds
028
Text and typography
029
Conclusion and next steps
Learn
Learn CSS!
Share
023
Blend Modes
Create compositional effects by mixing two or more layers, and learn how to isolate an image with a white background in this module on blend modes.

On this page
What is a blend mode?
Browser compatibility
mix-blend-mode
background-blend-mode
Separable blend modes
Normal
Multiply
Screen
Overlay
Darken
Lighten
Color dodge
Color burn
Hard light
Soft light
Difference
Exclusion
Non-separable blend modes
Hue
Saturation
Color
Luminosity
The isolation property


The CSS Podcast - 024: Blend Modes
Duotone is a popular color treatment for photography which makes an image look like it is only made up of two contrasting colors: one for highlights and the other for lowlights. How do you do this with CSS though?


Using blend modes—and other techniques you have learned about, such as filters and pseudo-elements—you can apply this effect to any image.

What is a blend mode? #
Blend modes are commonly used in design tools such as Photoshop to create a compositional effect by mixing colors from two or more layers. By changing how colors mix, you can achieve really interesting visual effects. You can also use blend modes as a utility, such as isolating an image that has a white background, so it appears to have a transparent background.


You can use most of the blend modes available in a design tool with CSS, using the mix-blend-mode or the background-blend-mode properties. The mix-blend-mode applies blending to a whole element and the background-blend-mode applies blending to the background of an element.

You use background-blend-mode when you have multiple backgrounds on an element and want them all to blend into each other.


The mix-blend-mode affects the entire element, including its pseudo-elements. One use-case is in the initial example of a duotone image, which has color layers applied to the element through its pseudo-elements.


Blend modes fall into two categories: separable and non-separable. A separable blend mode considers each color component, such as RGB, individually. A non-separable blend mode considers all color components equally.

Browser compatibility #
mix-blend-mode #
Browser support
41
32
79
8
Source
background-blend-mode #
Browser support
35
30
79
8
Source
Separable blend modes #
Normal #
This is the default blend mode and changes nothing about how an element blends with others.

Multiply #
The multiply blend mode is like stacking multiple transparencies on top of each other. White pixels will appear transparent, and black pixels will appear black. Anything in between will multiply its luminosity (light) values. This means lights get much lighter and darks, darker—most often producing a darker result.


.my-element {
  mix-blend-mode: multiply;
}

Screen #
Using screen multiplies the light values—an inverse effect to multiply, and will most often produce a brighter result.


.my-element {
  mix-blend-mode: screen;
}

Overlay #
This blend mode—overlay—combines multiply and screen. Base dark colors become darker and base light colors become lighter. Mid-range colors, such as a 50% gray, are unaffected.


.my-element {
  mix-blend-mode: overlay;
}

Darken #
The darken blend mode compares the source image and backdrop image's dark color luminosity and selects the darkest of the two. It does this by comparing rgb values instead of luminosity (like multiply and screen would do), for each color channel. With darken and lighten, new color values are often created from this comparison process.


.my-element {
  mix-blend-mode: darken;
}

Lighten #
Using lighten does the exact opposite of darken.


.my-element {
  mix-blend-mode: lighten;
}

Color dodge #
If you use color-dodge, it lightens the background color to reflect the source color. Pure black colors see no effect from this mode.


.my-element {
  mix-blend-mode: color-dodge;
}

Color burn #
The color-burn blend mode is very similar to the multiply blend mode, but increases contrast, resulting in more saturated mid-tones and reduced highlights.


.my-element {
  mix-blend-mode: color-burn;
}

Hard light #
Using hard-light creates a vivid contrast. This blend mode either screens or multiplies luminosity values. If the pixel value is lighter than 50% gray, the image is lightened, as if it were screened. If it is darker, it's multiplied.


.my-element {
  mix-blend-mode: hard-light;
}

Soft light #
The soft-light blend mode is a less-harsh version of overlay. It works in very much the same way with less contrast.


.my-element {
  mix-blend-mode: soft-light;
}

Difference #
A good way to picture how difference works is a bit like how a photo negative works. The difference blend mode takes the difference value of each pixel, inverting light colors. If the color values are identical, they become black. Differences in the values will invert.


.my-element {
  mix-blend-mode: difference;
}

Exclusion #
Using exclusion is very similar to difference, but instead of returning black for identical pixels, it will return 50% gray, resulting in a softer output with less contrast.


.my-element {
  mix-blend-mode: exclusion;
}

Non-separable blend modes #
You can think of these blend modes like HSL color components. Each takes a specific component value from the active layer and mixes it with other component values.

Hue #
The hue blend mode takes the hue of the source color and applies it to the saturation and luminosity of the backdrop color.


.my-element {
  mix-blend-mode: hue;
}

Saturation #
This works like hue, but using saturation as the blend mode applies the saturation of the source color to the hue and luminosity of the backdrop color.


.my-element {
  mix-blend-mode: saturation;
}

Color #
The color blend mode will create a color from the hue and saturation of the source color and the luminosity of the backdrop color.


.my-element {
  mix-blend-mode: color;
}

Luminosity #
Lastly, luminosity is the inverse of color. It creates a color with the luminosity of the source color and the hue and saturation of the backdrop color.


.my-element {
  mix-blend-mode: luminosity;
}

The isolation property #
Browser support
41
36
79
8
Source
If you set the isolation property to have a value of isolate, it will create a new stacking context, which will prevent it from blending with a backdrop layer. As you learned in the z-index module, when you create a new stacking context, that layer becomes the base layer. This means that parent-level blend modes will no longer apply, but elements inside of an element with isolation: isolate set can still blend.

Note that this doesn't work with background-blend-mode because the background property is already isolated.


Check your understanding
Test your knowledge of blend-modes
QUESTION 1
QUESTION 2
Which of following are CSS blend modes?



Difference

Lighten

Brighten

Dullen

Multiply

Overlay
CHECK
PREV
022
Filters
NEXT
024
Lists
A list, structurally, is composed of a list container element filled with list items. In this module, you'll learn how to style all the parts of a list.

We want to help you build beautiful, accessible, fast, and secure websites that work cross-browser, and for all of your users. This site is our home for content to help you on that journey, written by members of the Chrome team, and external experts.

Contribute
File a bug
View source
Related content
developer.chrome.com
Chrome updates
Case studies
Podcasts
Shows
Connect
Twitter
YouTube
Google Developers
Chrome
Firebase
Google Cloud Platform
All products
Dark theme


ENGLISH (en)
Terms & Privacy
Community Guidelines
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies.

By
Chrome DevRel
}
