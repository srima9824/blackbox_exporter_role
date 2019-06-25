Role Name: blackbox_exporter
=========

This role is for installing and configuring blackbox exporter on the systems.

Role Variables
--------------

In the defaults , main.yml file, blackbox_exporter_version variable can be changed to download the required version of blackbox exporter

Example Playbook
----------------



    - hosts: webservers
      become: true
      roles:
         - blackbox_exporter


