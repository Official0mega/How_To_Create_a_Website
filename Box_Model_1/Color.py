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
006
Color
There are several different ways to specify color in CSS. In this module we take a look at the most commonly used color values.

On this page

The CSS Podcast - 006: Color Part One
Color is an important part of any website and in CSS there are many options for color types, functions and treatments.

How do you decide which color type to use? How do you make your colors semi-transparent? In this lesson, you're going to learn which options you have to help you make the right decisions for your project and team.

CSS has various different data types, such as strings and numbers. Color is one of these types and uses other types, such as numbers for its own definitions.

Numeric colors #
It is very likely that your first exposure to colors in CSS is via numeric colors. We can work with numerical color values in a few different forms.

Hex colors #

h1 {
  color: #b71540;
}
Hexadecimal notation (often shortened to hex) is a shorthand syntax for RGB, which assigns a numeric value to red green and blue, which are the three primary colors.

According to the Web Almanac, hex is the most popular color syntax type.
The hexadecimal ranges are 0-9 and A-F. When used in a six digit sequence, they are translated to the RGB numerical ranges which are 0-255 which correspond to the red, green, and blue color channels respectively.


You can also define an alpha value with any numerical colors. An alpha value is a percentage of transparency. In hex code, you add another two digits to the six digit sequence, making an eight digit sequence. For example, to set black in hex code, write #000000. To add a 50% transparency, change it to #00000080.

Because the hex scale is 0-9 and A-F, the transparency values are probably not quite what you'd expect them to be. Here are some key, common values added to the black hex code, #000000:

0% alpha—which is fully transparent—is 00: #00000000
50% alpha is 80: #00000080
75% alpha is BF: #000000BF

To convert a two digit hex to a decimal, take the first digit and multiply it by 16 (because hex is base 16), then add the second digit. Using BF as an example for 75% alpha:

B is equal to 11, which when multiplied by 16 equals 176
F is equal to 15
176 + 15 = 191
The alpha value is 191—75% of 255
You can also write hex codes in a three digit shorthand. A three digit hex code is a shortcut to an equivalent six digit sequence. For example, #a4e is identical to #aa44ee. To add alpha, then #a4e8 would expand to #aa44ee88.
RGB (Red, Green, Blue) #

h1 {
  color: rgb(183, 21, 64);
}
RGB colors are defined with the rgb() color function, using either numbers or percentages as parameters. The numbers need to be within the 0-255 range and the percentages are between 0% and 100%‌. RGB works on the 0-255 scale, so 255 would be equivalent to 100%, and 0 to 0%.

To set black in RGB, define it as rgb(0 0 0), which is zero red, zero green and zero blue. Black can also be defined as rgb(0%, 0%, 0%). White is the exact opposite: rgb(255, 255, 255) or rgb(100%, 100%, 100%).

An alpha is set in rgb() in one of two ways. Either add a / after the red, green and blue parameters, or use the rgba() function. The alpha can be defined with a percentage or a decimal between 0 and 1. For example, to set a 50% alpha black in modern browsers, write: rgb(0 0 0 / 50%) or rgb(0 0 0 / 0.5). For wider support, using the rgba() function, write: rgba(0, 0, 0, 50%) or rgba(0, 0, 0, 0.5).


Commas were removed from the rgb() and hsl() notation because newer color functions, such as lab() and lch() use spaces instead of commas as a delimiter. This change provides more consistency not just with newer color functions, but with CSS in general. For better backwards compatibility, you can still use commas to define rgb() and hsl().
HSL (Hue, Saturation, Lightness) #

h1 {
  color: hsl(344, 79%, 40%);
}
HSL stands for hue, saturation and lightness. Hue describes the value on the color wheel, from 0 to 360 degrees, starting with red (being both 0 and 360). A hue of 180, or 50% would be in the blue range. It's the origin of the color that we see.

A color wheel with labels for degree values in 60 degree increments to help visuals what each angle value represents
Saturation is how vibrant the selected hue is. A fully desaturated color (with a saturation of 0%) will appear grayscale. And finally, lightness is the parameter which describes the scale from white to black of added light. A lightness of 100% will always give you white.

Using the hsl() color function, you define a true black by writing hsl(0 0% 0%), or even hsl(0deg 0% 0%). This is because the hue parameter defines the degree on the color wheel, which if you use the number type, is 0-360. You can also use the angle type, which is (0deg) or (0turn). Both saturation and lightness are defined with percentages.

The HSL color function broken down visually. The hue uses the color wheel. The saturation shows grey blending into teal. The lightness shows black into white.
The angle type in CSS is great for defining hue because it represents the angle of the color wheel really well. This type accepts degrees, turns, radians and gradians.
Browser support
2
3.6
12
4
Source

Alpha is defined in hsl(), in the same way as rgb() by adding a / after the hue, saturation and lightness parameters or by using the hsla() function. The alpha can be defined with a percentage or a decimal between 0 and 1. For example, to set a 50% alpha black, use: hsl(0 0% 0% / 50%) or hsl(0 0% 0% / 0.5). Using the hsla() function, write: hsla(0, 0%, 0%, 50%) or hsla(0, 0%, 0%, 0.5).

There are some newer color types coming to CSS. These include lab() and lch(), which allow a far wider range of color to be specified than is possible in RGB.
Color Keywords #
There are 148 named colors in CSS. These are plain English names such as purple, tomato and goldenrod. Some of the most popular names, according to the Web Almanac, are black, white, red, blue and gray. Our favorites include goldenrod, aliceblue, and hotpink.


Aside from standard colors, there are also special keywords available:

transparent is a fully transparent color. It is also the initial value of background-color
currentColor is the contextual computed dynamic value of the color property. If you have a text color of red and then set the border-color to be currentColor, it will also be red. If the element that you define currentColor on doesn't have a value for color defined, currentColor will be computed by the cascade instead
System keywords are colors that are defined by your operating system theme. Some examples of these colors are Background, which is the desktop background color or Highlight, which is the highlight color of selected items. These are just two of many options. All color keywords are case-insensitive, however you will often see system colors with capitalization to differentiate them from standard color keywords.
Where to use color in CSS rules #
If a CSS property accepts the <color> data type as a value, it will accept any of the above methods of expressing color. For styling text, use the color, text-shadow and text-decoration-color properties which all accept color as the value or color as part of the value.

For backgrounds, you can set a color as the value for background or background-color. Colors can also be used in gradients, such as linear-gradient. Gradients are a type of image that can be programmatically defined in CSS. Gradients accept two or more colors in any combination of color format, such as hex, rgb or hsl.

There's lots to learn with gradients so we wrote a whole lesson on how to use them.
Finally, border-color, and outline-color set the color for borders and outlines on your boxes. The box-shadow property also accepts color as one of the values.


Check your understanding
Test your knowledge of color
QUESTION 1
QUESTION 2
Which of the following are valid colors?



rbga(400 0 1)

#0f08

#OOFZ2

rgb(255, 0, 0)

hsl(180deg 50% 50%)

hotpink
CHECK
Resources #
A handy demo showing how you can use angles with HSL
A comprehensive guide on color
[video] An explainer on how to read hex codes
How hexadecimal codes work
PREV
005
Inheritance
NEXT
007
Sizing Units
In this module find out how to size elements using CSS, working with the flexible medium of the web.

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
