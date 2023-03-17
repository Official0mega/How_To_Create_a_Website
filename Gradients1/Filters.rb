#include <iostream>
int main()
{

Open menu
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
022
Filters
Filters in CSS mean that you can apply effects you might only think possible in a graphics application. In this module, you can discover what is available.

On this page

The CSS Podcast - 023: Filters
Say you need to build an element that's got a slightly opaque, frosted glass effect that sits over the top of an image. The text needs to be live text and not an image. How do you do that?


A combination of CSS filters and the backdrop-filter allow us to apply effects and blur what's needed in real time. Blur and opacity are two of many available filters, so let's have a quick run through what they all do and how to use them.

Take care when placing text over images, that the text is still readable should the filter effect not be supported in a user's browser. For example, at the moment backdrop-filter is not supported in Firefox, and so you should check that Firefox users aren't left with text they cannot easily read:
Browser support
76
103
17
9
Source
The filter property #
Browser support
53
35
12
9.1
Source
You can apply one or many of the following filters as a value for filter. If you incorrectly apply a filter, the rest of the filters defined for filter will not work.

blur #
This applies a gaussian blur and the only argument you can pass is a radius, which is how much blur is applied. This needs to be a length unit, like 10px. Percentages are not accepted.


.my-element {
	filter: blur(0.2em);
}

brightness #
Browser support
18
35
12
6
Source
To increase or decrease the brightness of an element, use the brightness function. The brightness value is expressed as a percentage with the unchanged image being expressed as a value of 100%. A value of 0% turns the image completely black, therefore values between 0% and 100% make the image less bright. Use values over 100% to increase the brightness.


.my-element {
	filter: brightness(80%);
}
You can also use decimal values, instead of percentage values in filters like brightness. To set 80% brightness with a decimal, write 0.8.

contrast #
Browser support
18
35
12
6
Source
Set a value between 0% and 100% to decrease or increase the contrast, respectively.


.my-element {
	filter: contrast(160%);
}

grayscale #
Browser support
18
35
12
6
Source
You can apply a completely grayscale effect by using 1 as a value for grayscale(), or 0 to have a completely saturated element. You can also use percentage or decimal values to only apply a partial grayscale effect. If you pass no arguments, the element will be completely grayscale. If you pass a value greater than 100%, it will be capped at 100%.


.my-element {
	filter: grayscale(80%);
}

invert #
Browser support
18
35
12
6
Source
Just like grayscale, you can pass 1 or 0 to the invert() function to turn it on or off. When it is on, the element's colors are completely inverted. You can also use percentage or decimal values to only apply a partial inversion of colors. If you don't pass any arguments into the invert() function, the element will be completely inverted.


.my-element {
	filter: invert(1);
}

opacity #
Browser support
18
35
12
6
Source
The opacity() filter works just like the opacity property, where you can pass a number or percentage to increase or reduce opacity. If you pass no arguments, the element is fully visible.


.my-element {
	filter: opacity(0.3);
}

saturate #
Browser support
18
35
12
6
Source
The saturate filter is very similar to the brightness filter and accepts the same argument: number or percentage. Instead of increasing or decreasing the brightness effect, saturate increases or decreases color saturation.


.my-element {
   filter: saturate(155%);
}

sepia #
Browser support
18
35
12
6
Source
You can add a sepia tone effect with this filter that works like grayscale(). The sepia tone is a photographic printing technique that converts black tones to brown tones to warm them up. You can pass a number or percentage as the argument for sepia() which increases or decreases the effect. Passing no arguments adds a full sepia effect (equivalent to sepia(100%)).


.my-element {
	filter: sepia(70%);
}

hue-rotate #
Browser support
18
35
12
6
Source
You learned about how the hue in hsl references a rotation of the color wheel in the colors lesson and this filter works in a similar way. If you pass an angle, such as degrees or turns, it shifts the hue of all the element's colors, changing the part of the color wheel it references. If you pass no argument, it does nothing.


.my-element {
	filter: hue-rotate(120deg);
}

drop-shadow #
Browser support
18
35
12
6
Source
You can apply a curve-hugging drop shadow like you would in a design tool, such as Photoshop with drop-shadow. This shadow is applied to an alpha mask which makes it very useful for adding a shadow to a cutout image. The drop-shadow filter takes a shadow parameter which contains space separated offset-x, offset-y, blur and color values. It is almost identical to box-shadow, but the inset keyword and spread value are not supported.


.my-element {
	filter: drop-shadow(5px 5px 10px orange);
}

Learn more about the different types of shadows in the shadows module.

url #
Browser support
1
4
12
3
Source
The url filter allows you to apply an SVG filter from a linked SVG element or file. You can read more about SVG filters here


Backdrop filter #
Browser support
76
103
17
9
Source
The backdrop-filter property accepts all of the same filter function values as filter. The difference between backdrop-filter and filter is that the backdrop-filter property only applies the filters to the background, where the filter property applies it to the whole element.

The example right at the start of this lesson is the perfect example, because you don't want the text to be blurred and ideally you don't want to have to add extra HTML elements. Being able to apply filters only to the backdrop enables that.


Check your understanding
Test your knowledge of filters
QUESTION 1
QUESTION 2
Which of following are CSS filter functions?



grayscale()

invert()

flip()

multiply()

blur()

brightness()
CHECK
PREV
021
Animations
NEXT
023
Blend Modes
Create compositional effects by mixing two or more layers, and learn how to isolate an image with a white background in this module on blend modes.

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
