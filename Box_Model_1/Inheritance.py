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
005
Inheritance
Some CSS properties inherit if you don't specify a value for them. Find out how this works, and how to use it to your advantage in this module.

On this page

The CSS Podcast - 005: Inheritance
Say you just wrote some CSS to make elements look like a button.


<a href="http://example.com" class="my-button">I am a button link</a>

.my-button {
  display: inline-block;
  padding: 1rem 2rem;
  text-decoration: none;
  background: pink;
  font: inherit;
  text-align: center;
}
You then add a link element to an article of content, with a class value of .my-button. However there's an issue, the text is not the color that you expected it to be. How did this happen?

Some CSS properties inherit if you don't specify a value for them. In the case of this button, it inherited the color from this CSS:


article a {
  color: maroon;
}
In this lesson you'll learn why that happens and how inheritance is a powerful feature to help you write less CSS.


Inheritance flow #
Let's take a look at how inheritance works, using this snippet of HTML:


<html>
  <body>
    <article>
      <p>Lorem ipsum dolor sit amet.</p>
    </article>
  </body>
</html>
The root element (<html>) won't inherit anything because it is the first element in the document. Add some CSS on the HTML element, and it starts to cascade down the document.


html {
  color: lightslategray;
}

The color property is inheritable by other elements. The html element has color: lightslategray, therefore all elements that can inherit color will now have a color of lightslategray.


body {
  font-size: 1.2em;
}

Because this demo sets the font size on the body element, the html element will still have the initial font size set by the browser (user agent stylesheet), but the article and p will inherit the font size declared by the body. This is because inheritance only cascades downwards.

p {
  font-style: italic;
}
Only the <p> will have italic text because it's the deepest nested element. Inheritance only flows downwards, not back up to parent elements.


Which properties are inheritable? #
Not all CSS properties are inheritable, but there are a lot that are. For reference, here is the entire list of inheritable properties, taken from the W3 reference of all CSS properties:

azimuth
border-collapse
border-spacing
caption-side
color
cursor
direction
empty-cells
font-family
font-size
font-style
font-variant
font-weight
font
letter-spacing
line-height
list-style-image
list-style-position
list-style-type
list-style
orphans
quotes
text-align
text-indent
text-transform
visibility
white-space
widows
word-spacing
How inheritance works #
Every HTML element has every CSS property defined by default with an initial value. An initial value is a property that's not inherited and shows up as a default if the cascade fails to calculate a value for that element.

Properties that can be inherited cascade downwards, and child elements will get a computed value which represents its parent's value. This means that if a parent has font-weight set to bold all child elements will be bold, unless their font-weight is set to a different value, or the user agent stylesheet has a value for font-weight for that element.


How to explicitly inherit and control inheritance #
Inheritance can affect elements in unexpected ways so CSS has tools to help with that.

The inherit keyword #
You can make any property inherit its parent's computed value with the inherit keyword. A useful way to use this keyword is to create exceptions.


strong {
  font-weight: 900;
}
This CSS snippet sets all <strong> elements to have a font-weight of 900, instead of the default bold value, which would be the equivalent of font-weight: 700.


.my-component {
  font-weight: 500;
}
The .my-component class sets font-weight to 500 instead. To make the <strong> elements inside .my-component also font-weight: 500 add:


.my-component strong {
  font-weight: inherit;
}

Now, the <strong> elements inside .my-component will have a font-weight of 500.

You could explicitly set this value, but if you use inherit and the CSS of .my-component changes in the future, you can guarantee that your <strong> will automatically stay up to date with it.

The initial keyword #
Inheritance can cause problems with your elements and initial provides you with a powerful reset option.

You learned earlier that every property has a default value in CSS. The initial keyword sets a property back to that initial, default value.


aside strong {
  font-weight: initial;
}
This snippet will remove the bold weight from all <strong> elements inside an <aside> element and instead, make them normal weight, which is the initial value.


The unset keyword #
The unset property behaves differently if a property is inheritable or not. If a property is inheritable, the unset keyword will be the same as inherit. If the property is not inheritable, the unset keyword is equal to initial.

Remembering which CSS properties are inheritable can be hard, unset can be helpful in that context. For example, color is inheritable, but margin isn't, so you can write this:


/* Global color styles for paragraph in authored CSS */
p {
  margin-top: 2em;
  color: goldenrod;
}

/* The p needs to be reset in asides, so you can use unset */
aside p {
  margin: unset;
  color: unset;
}

Now, the margin is removed and color reverts back to being the inherited computed value.

You can use the unset value with the all property, too. Going back to the above example, what happens if the global p styles get an additional few properties? Only the rule that was set for margin and color will apply.


/* Global color styles for paragraph in authored CSS */
p {
	margin-top: 2em;
	color: goldenrod;
	padding: 2em;
	border: 1px solid;
}

/* Not all properties are accounted for anymore */
aside p {
	margin: unset;
	color: unset;
}

If you change the aside p rule to all: unset instead, it doesn't matter what global styles are applied to p in the future, they will always be unset.


aside p {
	margin: unset;
	color: unset;
	all: unset;
}

Check your understanding
Test your knowledge of inheritance
QUESTION 1
QUESTION 2
Which of the following properties are inheritable?



animation

font-size

color

text-align

line-height
CHECK
Resources #
MDN reference on computed values
An article on how inheritance can be useful in modular front-ends
PREV
004
Specificity
NEXT
006
Color
There are several different ways to specify color in CSS. In this module we take a look at the most commonly used color values.

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
