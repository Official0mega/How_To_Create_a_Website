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
004
Specificity
This module takes a deeper look at specificity, a key part of the cascade.

On this page

The CSS Podcast - 003: Specificity
Suppose that you're working with the following HTML and CSS:


<button class="branding">Hello, Specificity!</button>

button {
  color: red;
}

.branding {
  color: blue;
}
There's two competing rules here. One will color the button red and the other will color it blue. Which rule gets applied to the element? Understanding the CSS specification's algorithm about specificity is the key to understanding how CSS decides between competing rules.

Specificity is one of the four distinct stages of the cascade, which was covered in the last module, on the cascade.


Specificity scoring #
Each selector rule gets a scoring. You can think of specificity as a total score and each selector type earns points towards that score. The selector with the highest score wins.

With specificity in a real project, the balancing act is making sure the CSS rules you expect to apply, actually do apply, while generally keeping scores low to prevent complexity. The score should only be as high as we need it to be, rather than aiming for the highest score possible. In the future, some genuinely more important CSS might need to be applied. If you go for the highest score, you'll make that job hard.

Scoring each selector type #
Each selector type earns points. You add all of these points up to calculate a selector's overall specificity.

Universal selector #
A universal selector (*) has no specificity and gets 0 points. This means that any rule with 1 or more points will override it


* {
  color: red;
}
Element or pseudo-element selector #
An element (type) or pseudo-element selector gets 1 point of specificity .

Type selector #

div {
  color: red;
}
Pseudo-element selector #

::selection {
  color: red;
}
Class, pseudo-class, or attribute selector #
A class, pseudo-class or attribute selector gets 10 points of specificity.

Class selector #

.my-class {
  color: red;
}
Pseudo-class selector #

:hover {
  color: red;
}
Attribute selector #

[href='#'] {
  color: red;
}
The :not() pseudo-class itself adds nothing to the specificity calculation. However, the selectors passed in as arguments do get added to the specificity calculation.


div:not(.my-class) {
  color: red;
}
This sample would have 11 points of specificity because it has one type selector (div) and one class inside the :not().

ID selector #
An ID selector gets 100 points of specificity, as long as you use an ID selector (#myID) and not an attribute selector ([id="myID"]).


#myID {
  color: red;
}
Inline style attribute #
CSS applied directly to the style attribute of the HTML element, gets a specificity score of 1,000 points. This means that in order to override it in CSS, you have to write an extremely specific selector.


<div style="color: red"></div>
!important rule #
Lastly, an !important at the end of a CSS value gets a specificity score of 10,000 points. This is the highest specificity that one individual item can get.

An !important rule is applied to a CSS property, so everything in the overall rule (selector and properties) does not get the same specificity score.


.my-class {
  color: red !important; /* 10,000 points */
  background: white; /* 10 points */
}
Check your understanding
What is the specificity score of a[href="#"]?



1

5

11
CHECK
Specificity in context #
The specificity of each selector that matches an element is added together. Consider this example HTML:


<a class="my-class another-class" href="#">A link</a>
This link has two classes on it. Add the following CSS, and it gets 1 point of specificity:


a {
  color: red;
}
Reference one of the classes in this rule, it now has 11 points of specificity:


a.my-class {
  color: green;
}
Add the other class to the selector, it now has 21 points of specificity:


a.my-class.another-class {
  color: rebeccapurple;
}
Add the href attribute to the selector, it now has 31 points of specificity:


a.my-class.another-class[href] {
  color: goldenrod;
}
Finally,add a :hover pseudo-class to all of that, the selector ends up with 41 points of specificity:


a.my-class.another-class[href]:hover {
  color: lightgrey;
}
Check your understanding
Which of the following selectors is worth 21 points?



article > section

article.card.dark

article:hover a[href]
CHECK
Visualizing specificity #
In diagrams and specificity calculators, the specificity is often visualized like this:

A diagram demonstrating most specific to least specific selectors
The left group is id selectors. The second group is class, attribute, and pseudo-class selectors. The final group is element and pseudo-element selectors.

For reference, the following selector is 0-4-1:


a.my-class.another-class[href]:hover {
  color: lightgrey;
}
Check your understanding
Which of the following selectors is 1-2-1?



section#specialty.dark

#specialty:hover li.dark

[data-state-rad].dark#specialty:hover

li#specialty section.dark
CHECK
Pragmatically increasing specificity #
Let's say we have some CSS that looks like this:


.my-button {
  background: blue;
}

button[onclick] {
  background: grey;
}
With HTML that looks like this:


<button class="my-button" onclick="alert('hello')">Click me</button>

The button has a grey background, because the second selector earns 11 points of specificity (0-1-1). This is because it has one type selector (button), which is 1 point and an attribute selector ([onclick]), which is 10 points.

The previous rule—.my-button—gets 10 points (0-1-0), because it has one class selector.

If you want to give this rule a boost, repeat the class selector like this:


.my-button.my-button {
  background: blue;
}

button[onclick] {
  background: grey;
}

Now, the button will have a blue background, because the new selector gets a specificity score of 20 points (0-2-0).

Caution

If you find that you are needing to boost specificity like this frequently, it may indicate that you are writing overly specific selectors. Consider whether you can refactor your CSS to reduce the specificity of other selectors to avoid this problem.
A matching specificity score sees the newest instance win #
Let's stay with the button example for now and switch the CSS around to this:


.my-button {
  background: blue;
}

[onclick] {
  background: grey;
}
The button has a grey background, because both selectors have an identical specificity score (0-1-0).


If you switch the rules in the source order, the button would then be blue.


[onclick] {
  background: grey;
}

.my-button {
  background: blue;
}

This is the only instance where newer CSS wins. To do so it must match the specificity of another selector that targets the same element.

Resources #
CSS SpeciFISHity
Specificity Calculator
MDN Specificity
Specifics on CSS Specificity
Another Specificity Calculator
PREV
003
The cascade
NEXT
005
Inheritance
Some CSS properties inherit if you don't specify a value for them. Find out how this works, and how to use it to your advantage in this module.

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
