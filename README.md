# livehealthy
## A handy tool for monitoring body mass index (BMI)




[Web Access](https://live-healthy.herokuapp.com/)

**livehealthy**  is written by Reza Nazarian for Code Institute Third Milestone project.

This website is made written by using **HTML**, **CSS**,  **Javascript** and **Python**.
***
## **Content**

* [Overview](#overview)
* [User Stories](#user-stories)
* [UX](#ux)
* [Features](#features)
* [Technologies used](#technologies-used)
* [Resources](#resources)
* [Testing](#testing)
* [Deployment](#deployment)
* [Acknowledgments](#acknowledgments)


## **Overview**

This website is develped based for a startup health service company by focusing on simplicity and practicality of the website . 
the visitors are expected to be a wide range of people from adults to youngstres to receive help in order to start new healthy physical life. The website tends to be simple elegant and at the same time its design is simple and practical. 
It shou8ld display the services and the mission at the first glance.

## **User Stories**

Website visitors include: 
* Those who are looking for getting help over overweight or underweight body status 
* Those clients who have eating disorders
* People who control their weight and eating habits after trying different methods
* People who believe in science and want to be treated based on the latest scientific researches


* A **General Clinic** wants to check if a there are a team of scietistsand professionals who can help their patients solving weight issue based on scientific facts.
* Many **individuals** Prefer to consult with scientists and specialist in regards to their health.
* As a **Gym Trainer** Need to give advise to clients who are searching for a complete solution to their weight and diet.
* **Normal citizens**  Who have never a scientific advise on their weight related issues. 
* **All users** Who are looking for an uptodate, and economically viable solution to their diet and weight related issues.
* **All users** Can talk to their specialist and communicate online and reach them easily.
* **All users** are able to check the center social media.

## **UX**

###  &nbsp; &nbsp; **a.Strategy**


###  &nbsp; &nbsp; **b.Scope**



### &nbsp; &nbsp; **c.Structure**

The website has three pages wnd a menu bar which links all pages together.

The website will be responsive. and its [wireframe](static/assets/wireframe/livehealthy_wireframe.pdf) shows the blueprint of the project. The pages are displayed on three devises (desktop, tablet and smart-phone)

### &nbsp; &nbsp; **d.Surface**

### &nbsp; &nbsp; &nbsp; **d.I.Color**



### &nbsp; &nbsp; &nbsp; **d.II.Typography**


### &nbsp; &nbsp; &nbsp; **d.III.Images**


## **Features**

**Navigation Bar**


**Home Page**

 [The home page](index.html) contains the company name and an introduction to the company. Then four main services are listed in picturial blocks with an overlaying text referring to the related services.

**Who we are**

[Who we are page](livehealthy.html) starts with a paragraph leveraging on the goals and objectives of the company and creates confidence. the offices then are listed in addresses and located on google map.

**Contact**

[The contact page](contact.html) the contact page lists the typical work stages that the clients goes through and an email form underneath. The email has few features as per the followings:

#### &nbsp; **A flash message** 
 A popup mesaage indicates if the visitor was able to sent a message successfuly and will be contactsed.

**Footer**

The footer incluudes links to social media company accounts and copyright sign. This footer repeats on all pages. The theme is  transparent icons in black or floralwhaite (depends on visibility) while changing the background color once hovered on by mouse.

## **Technologies Used**

## &nbsp; &nbsp; a. Languages

HTML, CSS and Javascript and Python and deployed to Heroku framework were used for the website.

## &nbsp; &nbsp; b. Associated technologies




## &nbsp; &nbsp; c. Workspace, version control, and Repository storage


* [Github](https://en.wikipedia.org/wiki/GitHub)  

   Github is used to make **Repositories** and for **Version Control**.
* [Gitpod](https://www.gitpod.io/)

   Gitpod is the main cloud-based editor for this project. Workspaces are made using the green Gitpod button in Github.

## &nbsp; &nbsp; d. Other tools

* [AutoPrefixer](https://autoprefixer.github.io/)

  AutoPrefixer is used to make the site compatible with all browsers.
* [W3C Validator](https://validator.w3.org/)

  W3C validator is used for testing HTML and CSS for the site.
* [JSHint](https://jshint.com/)  

  JSHint is used for testing javascript code for the site.
* [Am I Responsive](https://amiresponsive.co.uk/)

  Am I Responsive site is used to take a mockup screenshot of the project, which is attached at the beginning of this document.
* [Online Spelling Check](https://www.grammarly.com/)

   Grammarly is used to check spelling and grammatical errors.
 ***

## **Resources**

[Code Institute Course Content](https://courses.codeinstitute.net/program/FullstackWebDeveloper)- Main source of fundamental knowledge.

 * Code institute **Slack Community**- Main source of assistance.

 * [Stack Overflow](https://stackoverflow.com/)- General Resources.

 * [Youtube](https://www.youtube.com/)- General Resource.

 * [iColorpalette](https://icolorpalette.com/)- Find a relevant color palette for the site.

  * [Am I Responsive](http://ami.responsivedesign.is/)- Responsive website mockup image generator.
  
* [MDN Web Docs](https://developer.mozilla.org/en-US/)- General resources

* [Google Map Platform](https://developers.google.com/maps/documentation)- Setting Google map API

* [Email JS](https://www.emailjs.com/)- Setting Email

## **Testing**



[Responsiveness](http://ami.responsivedesign.is/)

* All pages are tested for responsiveness:

![Home page responsiveness](assets/images/readme/responsiveness_home.png)

![who we are  page responsiveness](assets/images/readme/responsiveness_whoweare.png)

![Contact  page responsiveness](assets/images/readme/responsiveness_contact.png)


**Checking Email**

A separate google email account is made for the website for the test of the projects.

* ![Confirmation Message](assets/images/readme/confirmation_message.png)

* ![Visitor Received Email](assets/images/readme/visitor_received_email_message.png)

* ![Cmpany Received Email](assets/images/readme/company_received_email_message.png) 




[W3C Markup Validation Service](https://validator.w3.org/)

* There was an error regrding cash-control setting and due to that the cashe-control setting was removed from the heading. The cash-control need to be investigated for proper setup.

* There is also error in regard to the positioning a div under a Ul and an span under ul which in both cases I found them work pretty well so I decided to leave them. The warning are minor and are related to the hyphens under a commented line which is neglegeble.

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

* has generated no errors or warnings

[JSHint](https://jshint.com/)

* both [sendemail.js](assets/js/sendemail.js) and [whoarewe.js](assets/js/whoarewe.js) have generated few warnings which could be ignored as the script works!

[Lighthouse testing ](https://www.webpagetest.org/lighthouse/)

The finished site was checked through Lighthouse Developer tool and the result found is attached here.
![image](assets/images/readme/lighthouse.png)

The best practices section showing `amber` because of low resolution of the images, which I kept purposefully to load the page faster.


## **Deployment**

This project is developed to Heroku using the **Github** Repository. Coding is done in the workspace provided by **Gitpod**.

Steps were taken to deploy the project
1. Log into [Github](https://github.com/).
2. Select [RNazarian1/livehealthy](https://rnazarian1.github.io/livehealthy/).
3. Go to settings on the top right and scroll down to Github Pages.
4. Under source link dropdown change the none to **master** branch.
5. The page will be refreshed automatically and we will have a link to the live **URL**.

To run locally, You can clone this repository directly in the editor of your choice by

`git clone` and adding the URL of the site.

`git clone https://rnazarian1.github.io/livehealthy/`

and the local clone will be created.
***



## **Acknowledgments**

Code Institute Slack community for 24/7 availability and support.
Online code institute Tutor support for excellent support.
Special thanks to the student Kiran Kumari Satyarthy for her suggestions.
***




















