#include <iostream>
using namespace std;

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
007
Sizing Units
In this module find out how to size elements using CSS, working with the flexible medium of the web.

On this page

The CSS Podcast - 008: Sizing Units
The web is a responsive medium, but sometimes you want to control its dimensions to improve the overall interface quality. A good example of this is limiting line lengths to improve readability. How would you do that in a flexible medium like the web?


For this case, you can use a ch unit, which is equal to the width of a "0" character in the rendered font at its computed size. This unit allows you to limit the width of text with a unit that's designed to size text, which in turn, allows predictable control regardless of the size of that text. The ch unit is one of a handful of units that are helpful for specific contexts like this example.

Numbers #
Numbers are used to define opacity, line-height and even for color channel values in rgb. Numbers are unitless integers (1, 2, 3, 100) and decimals (.1, .2, .3).

Numbers have meaning depending on their context. For example, when defining line-height, a number is representative of a ratio if you define it without a supporting unit:


p {
  font-size: 24px;
  line-height: 1.5;
}

In this example, 1.5 is equal to 150% of the p element's computed pixel font size. This means that if the p has a font-size of 24px, the line height will be computed as 36px.

It's a good idea to use a unitless value for line-height, rather than specifying a unit. As you learned in the inheritance module, font-size can be inherited. Defining a unitless line-height keeps the line-height relative to the font size. This provides a better experience than, say, line-height: 15px, which will not change and might look strange with certain font sizes.
Numbers can also be used in the following places:

When setting values for filters: filter: sepia(0.5) applies a 50% sepia filter to the element.
When setting opacity: opacity: 0.5 applies a 50% opacity.
In color channels: rgb(50, 50, 50), where the values 0-255 are acceptable to set a color value. See color lesson.
To transform an element: transform: scale(1.2) scales the element by 120% of its initial size.
Percentages #
When using a percentage in CSS you need to know how the percentage is calculated. For example,width is calculated as a percentage of the available width in the parent element.


div {
  width: 300px;
  height: 100px;
}

div p {
  width: 50%; 
}

In the above example, the width of div p is 150px, assuming that the layout uses the default box-sizing: content-box.

If you set margin or padding as a percentage, they will be a portion of the parent element's width, regardless of direction.


div {
  width: 300px;
  height: 100px;
}

div p {
  margin-top: 50%; /* calculated: 150px */
  padding-left: 50%; /* calculated: 150px */
}

In the above snippet, both the margin-top and padding-left will compute to 150px.


div {
  width: 300px;
  height: 100px;
}

div p {
  width: 50%; /* calculated: 150px */
  transform: translateX(10%); /* calculated: 15px */
}

If you set a transform value as a percentage, it is based on the element with the transform set. In this example, the p has a translateX value of 10% and a width of 50%. First, calculate what the width will be: 150px because it is 50% of its parent's width. Then, take 10% of 150px, which is 15px.

Key Term

The transform property allows you alter an element's appearance and position by rotating, skewing, scaling and translating it. This can be done in a 2D and 3D space.
Dimensions and lengths #
If you attach a unit to a number, it becomes a dimension. For example, 1rem is a dimension. In this context, the unit that is attached to a number is referred to in specifications as a dimension token. Lengths are dimensions that refer to distance and they can either be absolute or relative.

Absolute lengths #
All absolute lengths resolve against the same base, making them predictable wherever they're used in your CSS. For example, if you use cm to size your element and then print, it should be accurate if you compared it to a ruler.


div {
  width: 10cm;
  height: 5cm;
  background: black;
}
If you printed this page, the div would print as a 10x5cm black rectangle. Keep in mind, CSS is used not only for digital content, but also to style print content. Absolute lengths can really come in handy when designing for print.

Unit	Name	Equivalent to
cm	Centimeters	1cm = 96px/2.54
mm	Millimeters	1mm = 1/10th of 1cm
Q	Quarter-millimeters	1Q = 1/40th of 1cm
in	Inches	1in = 2.54cm = 96px
pc	Picas	1pc = 1/6th of 1in
pt	Points	1pt = 1/72th of 1in
px	Pixels	1px = 1/96th of 1in
Relative lengths #
A relative length is calculated against a base value, much like a percentage. The difference between these and percentages is that you can contextually size elements. This means that CSS has units such as ch that use the text size as a basis, and vw which is based on the width of the viewport (your browser window). Relative lengths are particularly useful on the web due to its responsive nature.

Font-size-relative units #
CSS provides helpful units that are relative to the size of elements of rendered typography, such as the size of the text itself (em units) or width of the typefaces characters (ch units).

unit	relative to:
em	Relative to the font size, i.e. 1.5em will be 50% larger than the base computed font size of its parent. (Historically, the height of the capital letter "M").
ex	Heuristic to determine whether to use the x-height, a letter "x", or `.5em` in the current computed font size of the element.
cap	Height of the capital letters in the current computed font size of the element.
ch	Average character advance of a narrow glyph in the element's font (represented by the "0" glyph).
ic	Average character advance of a full width glyph in the element's font, as represented by the "水" (CJK water ideograph, U+6C34) glyph.
rem	Font size of the root element (default is 16px).
lh	Line height of the element.
rlh	Line height of the root element.
The text, CSS is 10x great with labels for ascender height, descender height and x-height. The x-height represents 1ex and the 0 represents 1ch
Viewport-relative units #
You can use the dimensions of the viewport (browser window) as a relative basis. These units portion up the available viewport space.

unit	relative to
vw	1% of viewport's width. People use this unit to do cool font tricks, like resizing a header font based on the width of the page so as the user resizes, the font will also resize.
vh	1% of viewport's height. You can use this to arrange items in a UI, if you have a footer toolbar for example.
vi	1% of viewport's size in the root element's inline axis. Axis refers to writing modes. In horizontal writing modes like English, the inline axis is horizontal. In vertical writing modes like some Japanese typefaces, the inline axis runs top to bottom.
vb	1% of viewport's size in the root element's block axis. For the block axis, this would be the directionality of the language. LTR languages like English would have a vertical block axis, since English language readers parse the page from top to bottom. A vertical writing mode has a horizontal block axis.
vmin	1% of the viewport's smaller dimension.
vmax	1% of the viewport's larger dimension.

div {
  width: 10vw;
}

p {
  max-width: 60ch;
}

In this example, the div will be 10% of the viewport's width because 1vw is 1% of the viewport width. The p element has a max-width of 60ch which means it can't exceed the width of 60 "0" characters in the calculated font and size.

Objective

By sizing text with relative units like em or rem, rather than an absolute unit, like px, the size of your text can respond to user preferences. This can include the system font size or parent element's font size, such as the <body>. The base size of the em is the element's parent and the base size of the rem is the base font size of the document. If you don't define a font-size on your html element, this user-preferred system font size will be honoured if you use relative lengths, such as em and rem. If you use px units for sizing text, this preference will be ignored. 
Miscellaneous units #
There are some other units which have been specified to deal with particular types of values.

Angle units #
In the color module, we looked at angle units, which are helpful for defining degree values, such as the hue in hsl. They are also useful for rotating elements within transform functions.


div {
  width: 150px;
  height: 150px;
  transform: rotate(60deg);
}

Using the deg angle unit, you can rotate a div 90° on its center axis.


div {
  background-image: url('a-low-resolution-image.jpg');
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  div {
    background-image: url('a-high-resolution-image.jpg');
  }
}
Other angle units include rad (radians), grad (gradians), and turn units, which represent a part of an angle, where 1turn = 360deg, and 0.5turn = 180deg.
Resolution units #
In the previous example the value of min-resolution is 192dpi. The dpi unit stands for dots per inch. A useful context for this is detecting very high resolution screens, such as Retina displays in a media query and serving up a higher resolution image.

Check your understanding
Test your knowledge of sizing
QUESTION 1
QUESTION 2
QUESTION 3
Which of the following are valid dimensions?



cm

ui

in

8th

px

ch

ux

em

ex
CHECK
Resources #
CSS Spec Values and Units Level 4
Sizing and Units on MDN
All About Ems
A percentages explainer
PREV
006
Color
NEXT
008
Layout
An overview of the various layout methods you have to choose from when building a component or page layout.

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
