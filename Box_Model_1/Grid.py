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
010
Grid
CSS Grid Layout provides a two dimensional layout system, controlling layout in rows and columns. In this module discover everything grid has to offer.

On this page
Overview
Grid terminology
Grid lines
Grid tracks
Grid cell
Grid area
Gaps
Grid container
Grid item
Rows and columns
Intrinsic sizing keywords
The fr unit
The minmax() function
repeat() notation
auto-fill and auto-fit
Auto-placement
Placing items in columns
Spanning tracks
Filling gaps
Placing items
Stacking items
Negative line numbers
Named grid lines
Grid Template Areas
Shorthand properties
grid-template
grid property
Alignment
Distributing extra space
Moving content around
Resources


The CSS Podcast - 011: Grid
A really common layout in web design is a header, sidebar, body and footer layout.

A header with logo and navigation with a sidebar and content area that features an article
Over the years, there have been many methods to solve this layout, but with CSS grid, not only is it relatively straightforward, but you have lots of options. Grid is exceptionally useful at combining the control that extrinsic sizing provides with the flexibility of intrinsic sizing, which makes it ideal for this sort of layout. This is because grid is a layout method designed for two-dimensional content. That is, laying things out in rows and columns at the same time.

When creating a grid layout you define a grid with rows and columns. Then you place items onto that grid, or allow the browser to auto-place them into the cells you have created. There's a lot to grid, but with an overview of what is available you'll be making grid layouts in no time.

Overview #
So what can you do with grid? Grid layouts have the following features. You'll learn about all of them in this guide.

A grid can be defined with rows and columns. You can choose how to size these row and column tracks or they can react to the size of the content.
Direct children of the grid container will be automatically placed onto this grid.
Or, you can place the items in the precise location that you want.
Lines and areas on the grid can be named to make placement easier.
Spare space in the grid container can be distributed between the tracks.
Grid items can be aligned within their area.
Grid terminology #
Grid comes with a bunch of new terminology as it's the first time CSS has had a real layout system.

Grid lines #
A grid is made up of lines, which run horizontally and vertically. If your grid has four columns, it will have five column lines including the one after the last column.

Lines are numbered starting from 1, with the numbering following the writing mode and script direction of the component. This means that column line 1 will be on the left in a left-to-right language such as English, and on the right in a right-to-left language such as Arabic.

A diagram representation of grid lines
Grid tracks #
A track is the space between two grid lines. A row track is between two row lines and a column track between two column lines. When we create our grid we create these tracks by assigning a size to them.

A diagram representation of a grid track
Grid cell #
A grid cell is the smallest space on a grid defined by the intersection of row and column tracks. It's just like a table cell or a cell in a spreadsheet. If you define a grid and don't place any of the items they will automatically be laid out one item into each defined grid cell.

A diagram representation of a grid cell
Grid area #
Several grid cells together. Grid areas are created by causing an item to span over multiple tracks.

A diagram representation of a grid area
Gaps #
A gutter or alley between tracks. For sizing purposes these act like a regular track. You can't place content into a gap but you can span grid items across it.

A diagram representation of a grid with gaps
Grid container #
The HTML element which has display: grid applied, and therefore creates a new grid formatting context for the direct children.


.container {
  display: grid;
}
Grid item #
A grid item is an item which is a direct child of the grid container.


<div class="container">
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
</div>
Rows and columns #
To create a basic grid you can define a grid with three column tracks, two row tracks and a 10 pixel gap between the tracks as follows.


.container {
    display: grid;
    grid-template-columns: 5em 100px 30%;
    grid-template-rows: 200px auto;
    gap: 10px;
}
This grid demonstrates many of the things described in the terminology section. It has three column tracks. Each track uses a different length unit. It has two row tracks, one using a length unit and the other auto. When used as a track sizing auto can be thought of as being as big as the content. Tracks are auto sized by default.

If the element with a class of .container has child items, they will immediately lay out on this grid. You can see this in action in the demo below.


The grid overlay in Chrome DevTools can help you understand the various parts of the grid.

Open the demo in Chrome. Inspect the element with the grey background, which has an ID of container. Highlight the grid by selecting the grid badge in the DOM, next to the .container element. Inside the Layout tab, select Display Line Numbers in the dropdown to see the line numbers on your grid.

As described in the caption and instructions
A grid highlighted in Chrome DevTools showing line numbers, cells and tracks.
Intrinsic sizing keywords #
In addition to the length and percentage dimensions as described in the section on sizing units, grid tracks can use intrinsic sizing keywords. These keywords are defined in the Box Sizing specification and add additional methods of sizing boxes in CSS, not just grid tracks.

min-content
max-content
fit-content()
The min-content keyword will make a track as small as it can be without the track content overflowing. Changing the example grid layout to have three column tracks all at min-content size will mean they become as narrow as the longest word in the track.

The max-content keyword has the opposite effect. The track will become as wide enough for all of the content to display in one long unbroken string. This might cause overflows as the string will not wrap.

The fit-content() function acts like max-content at first. However, once the track reaches the size that you pass into the function, the content starts to wrap. So fit-content(10em) will create a track that is less than 10em, if the max-content size is less than 10em, but never larger than 10em.

In the next demo try out the different intrinsic sizing keywords by changing the sizing of the grid tracks.


You might spot in this demo that when auto is used the grid columns stretch to fill the container. Auto sized tracks will stretch by default if there is additional space in the grid container.
The fr unit #
We have existing length dimensions, percentages, and also these new keywords. There is also a special sizing method which only works in grid layout. This is the fr unit, a flexible length which describes a share of the available space in the grid container.

The fr unit works in a similar way to using flex: auto in flexbox. It distributes space after the items have been laid out. Therefore to have three columns which all get the same share of available space:


.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
As the fr unit shares out available space, it can be combined with a fixed size gap or fixed size tracks. To have a component with a fixed size element and the second track taking up whatever space is left, you can use as a tracklisting of grid-template-columns: 200px 1fr.

Using different values for the fr unit will share the space in proportion. Larger values getting more of the spare space. In the demo below change the value of the third track.


The minmax() function #
Browser support
57
52
16
10.1
Source
This function means that you can set a minimum and a maximum size for a track. This can be quite useful. If we take the example of the fr unit above which distributes remaining space, it could be written out using minmax() as minmax(auto, 1fr). Grid looks at the intrinsic size of the content, then distributes available space after giving the content enough room. This means that you might not get tracks that each have an equal share of all space available in the grid container.

To force a track to take an equal share of the space in the grid container minus gaps use minmax. Replace 1fr as a track size with minmax(0, 1fr). This makes the minimum size of the track 0 and not the min-content size. Grid will then take all of the available size in the container, deduct the size needed for any gaps, and share the rest out according to your fr units.

repeat() notation #
Browser support
57
76
16
10.1
Source
If you want to create a 12 column track grid with equal columns, you could use the following CSS.


.container {
    display: grid;
    grid-template-columns:
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr),
      minmax(0,1fr);
}
Or, you could write it out using repeat():


.container {
    display: grid;
    grid-template-columns: repeat(12, minmax(0,1fr));
}
The repeat() function can be used to repeat any section of your track listing. For example you can repeat a pattern of tracks. You can also have some regular tracks and a repeating section.


.container {
    display: grid;
    grid-template-columns: 200px repeat(2, 1fr 2fr) 200px; /*creates 6 tracks*/
}
auto-fill and auto-fit #
You can combine everything you have learned about track sizing, minmax(), and repeat, to create a useful pattern with grid layout. Perhaps you don't want to specify the number of column tracks, but instead want to create as many as will fit in your container.

You can achieve this with repeat() and the auto-fill or auto-fit keywords. In the demo below grid will create as many 200 pixel tracks as will fit in the container. Open the demo in a new window and see how the grid changes as you change the size of the viewport.


In the demo we get as many tracks as will fit. The tracks are not flexible however. You will get a gap on the end until there is enough space for another 200 pixel track. If you add the minmax() function, you can request as many tracks as will fit with a minimum size of 200 pixels and a maximum of 1fr. Grid then lays out the 200 pixel tracks and whatever space is leftover is distributed equally to them.

This creates a two-dimensional responsive layout with no need for any media queries.


There is a subtle difference between auto-fill and auto-fit. In the next demo play with a grid layout using the syntax explained above, but with only two grid items in the grid container. Using the auto-fill keyword you can see that empty tracks have been created. Change the keyword to auto-fit and the tracks collapse down to 0 size. This means that the flexible tracks now grow to consume the space.


The auto-fill and auto-fit keywords otherwise act in exactly the same way. There is no difference between them once the first track is filled.

Auto-placement #
You have already seen grid auto-placement at work in the demos so far. Items are placed on the grid one per cell in the order that they appear in the source. For many layouts this might be all you need. If you need more control then there are a couple of things you might like to do. The first is to tweak the auto-placement layout.

Placing items in columns #
The default behavior of grid layout is to place items along the rows. You can instead cause the items to place into columns using grid-auto-flow: column. You need to define row tracks otherwise the items will create intrinsic column tracks, and layout out all in one long row.

These values relate to the writing mode of the document. A row always runs in the direction a sentence runs in the writing mode of the document or component. In the next demo you can change mode the value of grid-auto-flow and the writing-mode property.


Spanning tracks #
You can cause some or all of the items in an auto-placed layout to span more than one track. Use the span keyword plus the number of lines to span as a value for grid-column-end or grid-row-end.


.item {
    grid-column-end: span 2; /* will span two lines, therefore covering two tracks */
}
As you have not specified a grid-column-start, this uses the initial value of auto and is placed according to the auto-placement rules. You can also specify the same thing using the shorthand grid-column:


.item {
    grid-column: auto / span 2;
}
Filling gaps #
An auto-placed layout with some items spanning multiple tracks may result in a grid with some unfilled cells. The default behavior of grid layout with a fully auto-placed layout is to always progress forward. The items will be placed according to the order they are in the source, or any modification with the order property. If there is not enough space to fit an item, grid will leave a gap and move to the next track.

The next demo shows this behavior. The checkbox will apply the dense packing mode. This is enabled by giving grid-auto-flow a value of dense. With this value in place, grid will take items later in the layout and use them to fill gaps. This may mean that the display becomes disconnected from the logical order.


Placing items #
You have a lot of functionality from CSS Grid already. Let's now take a look at how we position items on the grid we have created.

The first thing to remember is that CSS Grid Layout is based on a grid of numbered lines. The simplest way to place things onto the grid is to place them from one line to another. You'll discover other ways of placing items in this guide, but you always have access to those numbered lines.

The properties that you can use to place items by line number are:

grid-column-start
grid-column-end
grid-row-start
grid-row-end
They have shorthands which allow you to set both start and end lines at once:

grid-column
grid-row
To place your item set the start and end lines of the grid area that it should be placed into.


.container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 200px 100px);
}

.item {
    grid-column-start: 1; /* start at column line 1 */
    grid-column-end: 4; /* end at column line 4 */
    grid-row-start: 2; /*start at row line 2 */
    grid-row-end: 4; /* end at row line 4 */
}
Chrome DevTools can give you a visual guide to the lines in order to check where your item is placed.

The line numbering follows the writing mode and direction of the component. In the next demo change the writing mode or direction to see how the placement of the items stays consistent to the way that text flows.


Stacking items #
Using line-based positioning you can place items into the same cell of the grid. This means that you can stack items, or cause one item to partly overlap another. Items which come later in the source will be displayed on top of items that come earlier. You can change this stacking order using z-index just as with positioned items.


Negative line numbers #
When you create a grid using grid-template-rows and grid-template-columns you create what is known as the explicit grid. This is a grid that you have defined and given size to the tracks.

Sometimes you will have items which display outside this explicit grid. For example, you might define column tracks and then add several rows of grid items without ever defining row tracks. The tracks would be auto sized by default. You also might place an item using grid-column-end that is outside of the explicit grid defined. In both of these cases grid will create tracks to make the layout work, and these tracks are referred to as the implicit grid.

Most of the time it will make no difference if you are working with an implicit or explicit grid. However, with line-based placement you may run into the main difference between the two.

Using negative line numbers you can place items from the end line of the explicit grid. This can be useful if you want an item to span from the first to the last column line. In that case you can use grid-column: 1 / -1. The item will stretch right across the explicit grid.

This only works for the explicit grid however. Take a layout of three rows of auto-placed items where you would like the very first item to span to the end line of the grid.

A sidebar with 8 sibling grid items
You might think that you can give that item grid-row: 1 / -1. In the demo below you can see that this doesn't work. The tracks are created in the implicit grid, there is no way to reach the end of the grid using -1.


Sizing implicit tracks #
The tracks created in the implicit grid will be auto-sized by default. However if you want to control the sizing of the rows, use the grid-auto-rows property, and for columns grid-auto-columns.

To create all implicit rows at a minimum size of 10em and a maximum size of auto:


.container {
    display: grid;
    grid-auto-rows: minmax(10em, auto);
}
To create implicit columns with a pattern of 100px and 200px wide tracks. In this case the first implicit column will be 100px, the second 200px, the third 100px, and so on.


.container {
    display: grid;
    grid-auto-columns: 100px 200px;
}
Named grid lines #
It can make it easier to place items into a layout if the lines have a name rather than a number. You can name any line on your grid by adding a name of your choosing between square brackets. Multiple names can be added, separated by a space inside the same brackets. Once you have named lines they can be used instead of the numbers.


.container {
    display: grid;
    grid-template-columns:
      [main-start aside-start] 1fr
      [aside-end content-start] 2fr
      [content-end main-end]; /* a two column layout */
}

.sidebar {
    grid-column: aside-start / aside-end;
    /* placed between line 1 and 2*/
}

footer {
    grid-column: main-start / main-end;
    /* right across the layout from line 1 to line 3*/
}
Grid Template Areas #
You can also name areas of the grid and place items onto those named areas. This is a lovely technique as it allows you to see what your component looks like right there in the CSS.

To start, give the direct children of your grid container a name using the grid-area property:


header {
    grid-area: header;
}

.sidebar {
    grid-area: sidebar;
}

.content {
    grid-area: content;
}

footer {
    grid-area: footer;
}
The name can be anything you like other than the keywords auto and span. Once all of your items are named, use the grid-template-areas property to define which grid cells each item will span. Each row is defined within quotes.


.container {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    grid-template-areas:
        "header header header header"
        "sidebar content content content"
        "sidebar footer footer footer";
}
There are a few rules when using grid-template-areas.

The value must be a complete grid with no empty cells.
To span tracks repeat the name.
The areas created by repeating the name must be rectangular and cannot be disconnected.
If you break any of the above rules the value is treated as invalid and thrown away.

To leave white space on the grid use a . or multiples with no white space between them. For example to leave the very first cell on the grid empty I could add a series of . characters:


.container {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    grid-template-areas:
        "....... header header header"
        "sidebar content content content"
        "sidebar footer footer footer";
}
As your entire layout is defined in one place, it makes it straightforward to redefine the layout using media queries. In the next example I have created a two column layout which moves to three columns by redefining the value of grid-template-columns and grid-template-areas. Open the example in a new window to play with the viewport size and see the layout change.

You can also see how the grid-template-areas property relates to writing-mode and direction, as with other grid methods.


Shorthand properties #
There are two shorthand properties which allow you to set many of the grid properties in one go. These can look a little confusing until you break down exactly how they go together. Whether you want to use them or prefer to use longhands is up to you.

grid-template #
Browser support
57
52
16
10.1
Source
The grid-template property is a shorthand for grid-template-rows, grid-template-columns and grid-template-areas. The rows are defined first, along with the value of grid-template-areas. Column sizing is added after a /.


.container {
    display: grid;
    grid-template:
      "head head head" minmax(150px, auto)
      "sidebar content content" auto
      "sidebar footer footer" auto / 1fr 1fr 1fr;
}
grid property #
Browser support
57
52
16
10.1
Source
The grid shorthand can be used in exactly the same way as the grid-template shorthand. When used in this way it will reset the other grid properties that it accepts to their initial values. The full set being:

grid-template-rows
grid-template-columns
grid-template-areas
grid-auto-rows
grid-auto-columns
grid-auto-flow
You can alternately use this shorthand to define how the implicit grid behaves, for example:


.container {
    display: grid;
    grid: repeat(2, 80px) / auto-flow  120px;
}
Alignment #
Grid layout uses the same alignment properties that you learned about in the guide to flexbox. In grid the properties which begin with justify- are always used on the inline axis, the direction in which sentences run in your writing mode.

The properties which begin with align- are used on the block axis, the direction in which blocks are laid out in your writing mode.

justify-content and align-content: distribute additional space in the grid container around or between tracks.
justify-self and align-self: are applied to a grid item to move it around inside the grid area it is placed in.
justify-items and align-items: are applied to the grid container to set all of the justify-self properties on the items.
Distributing extra space #
In this demo the grid is larger than the space needed to lay out the fixed width tracks. This means we have space in both the inline and block dimensions of the grid. Try different values of align-content and justify-content to see how the tracks behave.


Note how the gaps become larger when using values such as space-between, and any grid item spanning two tracks also grows to absorb the additional space added to the gap.

As with flexbox, these properties will only work if there is additional space to distribute. If your grid tracks neatly fill the container then there will be no space to share out.
Moving content around #
Items with a background color appear to completely fill the grid area they are placed in, because the initial value for justify-self and align-self is stretch.

If your item is an image, or something else with an intrinsic aspect ratio, the initial value will be start rather than stretch to avoid stretching things out of shape.
In the demo change the values of justify-items and align-items to see how this changes the layout. The grid area is not changing size, instead the items are being moved around inside the defined area.


Check your understanding
Test your knowledge of grid
QUESTION 1
QUESTION 2
QUESTION 3
QUESTION 4
QUESTION 5
QUESTION 6
Which of the following are CSS grid terms?



lines

circles

cells

areas

trains

gaps

tracks
CHECK
Resources #
This guide has given you an overview of the different parts of the grid layout specification. To find out more, take a look at the following resources.

MDN CSS Grid Layout
A Complete Guide to Grid
Creating a Grid Container
Inspect CSS grid in Chrome DevTools
A comprehensive collection of grid learning material
PREV
009
Flexbox
NEXT
011
Logical Properties
Logical, flow relative properties and values are linked to the flow of text, rather than the physical shape of the screen. Learn how to take advantage of this newer approach to CSS.

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
