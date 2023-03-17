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
016
Shadows
There are a number of ways to add shadows to text and elements in CSS. In this module you'll learn how to use each option, and the tasks they were designed for.

On this page
Box shadow
Multiple shadows
Properties affecting box-shadow
Text shadow
Multiple shadows
Drop shadow


The CSS Podcast - 017: Shadows
Say you've been sent a design to build and in that design there's a picture of a t-shirt, cut out, with a drop shadow. The designer tells you that the product image is dynamic and can be updated via the content management system, so the drop shadow needs to be dynamic too. Instead of a t-shirt, the image could be a visor or shorts, or any other item. How do you do that with CSS?


CSS has the box-shadow and text-shadow properties, but the picture isn't text, so you can't use text-shadow. If you use box-shadow, the shadow is on the surrounding box, not around the t-shirt.


Luckily, there is another option: the drop-shadow() filter. This enables you to do exactly what the designer asked for. There are plenty of options when it comes to shadows in CSS, each designed for a different use case.

Box shadow #
Browser support
10
4
12
5.1
Source
The box-shadow property is for adding shadows to the box of an HTML element. It works on block elements and inline elements.


.my-element {
	box-shadow: 5px 5px 20px 5px #000;
}
The order of values for box-shadow are as follows:

Horizontal offset: a positive number pushes it out from the left and a negative number will push it out from the right.
Vertical offset: a positive number pushes it down from the top, and a negative number will push it up from the bottom.
Blur radius: a larger number produces a more blurred shadow, whereas a small number produces a sharper shadow.
Spread radius (optional): a larger number increases the size of the shadow and a smaller number decreases it, making it the same size as the blur radius if it's set to 0.
Color: Any valid color value. If this isn't defined, the computed text color will be used.
To make a box shadow an inner shadow, rather than the default outer shadow, add an inset keyword before the other properties.


/* Outer shadow */
.my-element {
	box-shadow: 5px 5px 20px 5px #000;
}

/* Inner shadow */
.my-element {
	box-shadow: inset 5px 5px 20px 5px #000;
}

Multiple shadows #
You can add as many shadows as you like with box-shadow. Add a comma separated collection of value sets to achieve this:


.my-element {
  box-shadow: 5px 5px 20px 5px darkslateblue, -5px -5px 20px 5px dodgerblue,
    inset 0px 0px 10px 2px darkslategray, inset 0px 0px 20px 10px steelblue;
}

Properties affecting box-shadow #
Adding a border-radius to your box will also affect the shape of the box shadow. This is because CSS is creating a shadow based on the shape of the box as if light is pointing at it.


.my-element {
  box-shadow: 0px 0px 20px 5px darkslateblue;
  border-radius: 25px;
}

If your box with box-shadow is in a container that has overflow: hidden, the shadow won't break out of that overflow either.


<div class="my-parent">
  <div class="my-shadow">My shadow is hidden by my parent.</div>
</div>

.my-parent,
.my-shadow {
  width: 250px;
  height: 250px;
}

.my-shadow {
  box-shadow: 0px 0px 20px 5px darkslateblue;
}

.my-parent {
  overflow: hidden;
}

Text shadow #
Browser support
2
3.5
12
1.1
Source
The text-shadow property is very similar to the box-shadow property. It only works on text nodes.


.my-element {
  text-shadow: 3px 3px 3px hotpink;
}
The values for text-shadow are the same as box-shadow and in the same order. The only difference is that text-shadow has no spread value and no inset keyword.


When you add a box-shadow it is clipped to the shape of your box, but text-shadow has no clipping. This means that if your text is fully or semi transparent, the shadow is visible through it.


.my-element {
  text-shadow: 3px 3px 3px gold;
  color: rgb(0 0 0 / 70%);
}

Multiple shadows #
You can add as many shadows as you like with text-shadow, just as with box-shadow. Add a comma separated collection of value sets, and you can create some really cool text effects, such as 3D text.


.my-element {
  text-shadow: 1px 1px 0px white,
    2px 2px 0px firebrick;
  color: darkslategray;
}

Drop shadow #
To achieve a drop shadow that follows any potential curves of an image, use the CSS drop-shadow filter. This shadow is applied to an alpha mask which makes it very useful for adding a shadow to a cutout image, as in the case in the intro of this module.


.my-image {
  filter: drop-shadow(0px 0px 10px rgba(0 0 0 / 30%))
}

Key Term

We cover CSS filters in another module, but in short, filters allow you to apply multiple graphical effects to the pixels of an element.
The drop-shadow filter has the same values as box-shadow but the inset keyword and spread value are not allowed. You can add as many shadows as you like, by adding multiple instances of drop-shadow values to the filter property. Each shadow will use the last shadow as a positioning reference point.


Check your understanding
Test your knowledge of shadows
QUESTION 1
QUESTION 2
Which shadow value below is unique to box-shadow?



Horizontal offset

Vertical offset

Blur radius

Spread radius

Color

inset
CHECK
PREV
015
Borders
NEXT
017
Focus
Understand the importance of focus in your web applications. You'll find out how to manage focus, and how to make sure the path through your page works for people using a mouse, and those using the keyboard to navigate.

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
