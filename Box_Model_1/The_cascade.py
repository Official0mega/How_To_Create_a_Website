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
003
The cascade
Sometimes two or more competing CSS rules could apply to an element. In this module find out how the browser chooses which to use, and how to control this selection.

On this page

The CSS Podcast - 004: The Cascade
CSS stands for Cascading Stylesheets. The cascade is the algorithm for solving conflicts where multiple CSS rules apply to an HTML element. It's the reason that the text of the button styled with the following CSS will be blue.


button {
  color: red;
}

button {
  color: blue;
}

Understanding the cascade algorithm helps you understand how the browser resolves conflicts like this. The cascade algorithm is split into 4 distinct stages.

Position and order of appearance: the order of which your CSS rules appear
Specificity: an algorithm which determines which CSS selector has the strongest match
Origin: the order of when CSS appears and where it comes from, whether that is a browser style, CSS from a browser extension, or your authored CSS
Importance: some CSS rules are weighted more heavily than others, especially with the !important rule type
Position and order of appearance #
The order in which your CSS rules appear and how they appear is taken into consideration by the cascade while it calculates conflict resolution.

The demo right at the start of this lesson is the most straightforward example of position. There are two rules that have selectors of identical specificity, so the last one to be declared won.

Styles can come from various sources on an HTML page, such as a <link> tag, an embedded <style> tag, and inline CSS as defined in an element's style attribute.

If you have a <link> that includes CSS at the top of your HTML page, then another <link> that includes CSS at the bottom of your page: the bottom <link> will have the most specificity. The same thing happens with embedded <style> elements, too. They get more specific, the further down the page they are.


The button has a blue background, as defined by CSS which is included by a <link /> element. A CSS rule that sets it to be dark is in a second linked stylesheet and is applied because of its later position.
This ordering also applies to embedded <style> elements. If they are declared before a <link>, the linked stylesheet's CSS will have the most specificity.


The <style> element is declared in the <head>, while the <link /> element is declared in the <body>. This means it gets more specificity than the <style> element
An inline style attribute with CSS declared in it will override all other CSS, regardless of its position, unless a declaration has !important defined.

Position also applies in the order of your CSS rule. In this example, the element will have a purple background because background: purple was declared last. Because the green background was declared before the purple background, it is now ignored by the browser.


.my-element {
  background: green;
  background: purple;
}
Being able to specify two values for the same property can be a simple way to create fallbacks for browsers that do not support a particular value. In this next example, font-size is declared twice. If clamp() is supported in the browser, then the previous font-size declaration will be discarded. If clamp() isn't supported by the browser, the initial declaration will be honored, and the font-size will be 1.5rem


.my-element {
  font-size: 1.5rem;
  font-size: clamp(1.5rem, 1rem + 3vw, 2rem);
}

This approach of declaring the same property twice works because browsers ignore values they don't understand. Unlike some other programming languages, CSS will not throw an error or break your program when it detects a line it cannot parse—the value it cannot parse is invalid and therefore ignored. The browser then continues to process the rest of the CSS without breaking stuff it already understands.
Check your understanding
If you have the following HTML on your page:


<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <button>I am a button</button>
    <style>
      button {
        background: pink;
      }
    </style>
  </body>
</html>
Inside styles.css, is the following CSS rule:


button {
  background: yellow;
}
What color is the button's background?



pink

yellow
CHECK
Specificity #
Specificity is an algorithm which determines which CSS selector is the most specific, using a weighting or scoring system to make those calculations. By making a rule more specific, you can cause it to be applied even if some other CSS that matches the selector appears later in the CSS.

In the next lesson you can learn the details of how specificity is calculated, however keeping a few things in mind will help you avoid too many specificity issues.

CSS targeting a class on an element will make that rule more specific, and therefore seen as more important to be applied, than CSS targeting the element alone. This means that with the following CSS, the h1 will be colored red even though both rules match and the rule for the h1 selector comes later in the stylesheet.


<h1 class="my-element">Heading</h1>

.my-element {
  color: red;
}

h1 {
  color: blue;
}
An id makes the CSS even more specific, so styles applied to an ID will override those applied many other ways. This is one reason why it is generally not a good idea to attach styles to an id. It can make it difficult to overwrite that style with something else.

Specificity is cumulative #
As you can find out in the next lesson, each type of selector is awarded points which indicate how specific it is, the points for all of the selectors you have used to target an element are added together. This means that if you target an element with a selector list such as a.my-class.another-class[href]:hover you get something quite hard to overwrite with other CSS. For this reason, and to help make your CSS more reusable, it's a good idea to keep your selectors as simple as possible. Use specificity as a tool to get at elements when you need to, but always consider refactoring long, specific selector lists, if you can.

Origin #
The CSS that you write isn't the only CSS applied to a page. The cascade takes into account the origin of the CSS. This origin includes the browser's internal stylesheet, styles added by browser extensions or the operating system, and your authored CSS. The order of specificity of these origins, from least specific, to most specific is as follows:

User agent base styles. These are the styles that your browser applies to HTML elements by default.
Local user styles. These can come from the operating system level, such as a base font size, or a preference of reduced motion. They can also come from browser extensions, such as a browser extension that allows a user to write their own custom CSS for a webpage.
Authored CSS. The CSS that you author.
Authored !important. Any !important that you add to your authored declarations.
Local user styles !important. Any !important that come from the operating system level, or browser extension level CSS.
User agent !important. Any !important that are defined in the default CSS, provided by the browser.
A visual demonstration of the order of origins as also explained in the list.
If you have an !important rule type in the CSS you have authored and the user has an !important rule type in their custom CSS, whose CSS wins?

Check your understanding
Test your knowledge of cascade origins, consider the following style rules from various origins:

User-agent style

h1 { margin-block-start: 0.83em; }
Bootstrap

h1 { margin-block-start: 20px; }
Page Author styles

h1 { margin-block-start: 2ch; }

@media (max-width: 480px) {
  h1 { margin-block-start: 1ch; }
}
User custom style

h1 { margin-block-start: 2rem !important; }
Then, given the following HTML:


<h1>Lorem ipsum</h1>
What is the final margin-block-start of the h1?



20px

0.83em

2rem

2ch

1ch
CHECK
Importance #
Not all CSS rules are calculated the same as each other, or given the same specificity as each other.

The order of importance, from least important, to most important is as follows:

normal rule type, such as font-size, background or color
animation rule type
!important rule type (following the same order as origin)
transition rule type
Active animation and transition rule types have higher importance than normal rules. In the case of transitions higher importance than !important rule types. This is because when an animation or transition becomes active, its expected behaviour is to change visual state.

Using DevTools to find out why some CSS is not applying #
Browser DevTools will typically show all CSS that could match an element, with those which are not being used crossed out.

An image of browser DevTools with overwritten CSS crossed out
If the CSS you expected to apply doesn't appear at all, then it didn't match the element. In that case you need to look elsewhere, perhaps for a typo in a class or element name or some invalid CSS.

Check your understanding
The Cascade can be used for...



Resolving conflicts when multiple styles apply to an element.

Ensuring there's only one style value for each property at draw time.

Scoring and weighting style rules.

Sorting and filtering style attributes.
CHECK
Resources #
A highly interactive explainer of the cascade
MDN cascade reference
PREV
002
Selectors
NEXT
004
Specificity
This module takes a deeper look at specificity, a key part of the cascade.

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
