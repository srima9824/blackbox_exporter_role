Introduction
=========

Installs and configures blackbox exporter service

Pre-Requisites
------------

Ansible version: 2.8.1
Python version: 2.7.15+

Variables
--------------

Defaults : main.yml

download_url: url to download blackbox exporter
blackbox_exporter_folder: folder to store the binary
binary_destination: shifting binary to usr/local/bin 
blackbox_exporter_download_location: location where blackbox exporter gets downloaded
blackbox_exporter_configuration_modules: configuration parameters of blackbox exporter

Example Playbook
----------------

---
- hosts: all
  become: true
  roles:
    - blackbox_exporter


License
-------

BSD

Author Information
------------------

Name: Srima Pal
Email: srima.pal@opstree.com
