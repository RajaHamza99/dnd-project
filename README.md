# DnD Project

## Contents

<ul>
  <li>Project Objective</li>
<li>App Overview</li>
<li>Asana Board</li>
<li>Database</li>
<li>CI Pipeline</li>
<li>App Design</li>
  <li>Deployment</li>
<li>Testing</li>
  <li>Risk Assessment</li>
<li>Current Issues</li>
<li>Improvements</li>
</ul>

## Project Objective
The requirements of the project are as follows:
<ul>
<li>An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.</li>
<li>An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.</li>
<li>If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.</li>
<li>The project must follow the Service-oriented architecture that has been asked for.</li>
<li>The project must be deployed using containerisation and an orchestration tool.</li>
<li>As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.</li>
<li>The project must make use of a reverse proxy to make your application accessible to the user.</li>
  
## App Overview
I created a Dnd Character Generation app. As part of having two implementations, the first one is simpler than the first.  

The first app will generate a random class, race and name for the user. 

The second app will generate the same, but also stats for the user's character. The second app also commits the character's class, race and name to a database which persists even after the containers are brought down through the use of a volume.  

## Asana Board
In order to keep track of my project and it's progress, I used an Asana board. This board also marks the items needed for the Minimum Viable Product (MVP). This also includes completed user stories to allow me to see what I would like the user to be able to do at bare minimum.

## Database
This application only requires a simple table to store information. The following table is used to store data:

## CI Pipeline
This first diagram is what I initially imagined the CI Pipeline to look like. 

This second diagram is what the finalised CI Pipeline looks like. It includes the use of Ansible to configure my machines and Nginx which works as both a reverse proxy and load balancer. 

##  App Design #1
