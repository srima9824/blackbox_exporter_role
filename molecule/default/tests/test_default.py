import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_user_exists(User):
    '''Check user exists'''
    user = User('blackbox_exporter')
    assert user.exists

def test_group_exists(Group):
    '''Check group exists'''
    group = Group('blackbox_exporter')
    assert group.exists

def test_blackbox_exporter_folder_creation(host):
    '''Check group exists'''
    host.file('/tmp/blackbox_exporter-0.12.0.linux-amd64/blackbox_exporter').is_directory

def test_blackbox_exporter_folder_exists(host):
    '''Check group exists'''
    host.file('/tmp/blackbox_exporter-0.12.0.linux-amd64/blackbox_exporter').exists

def test_binary_shifted(host):
    '''Check group exists'''
    host.file('/usr/local/bin/blackbox_exporter').exists

def test_configuration_file_created(host):
    '''Check if blackbox exporter configuration file created'''
    host.file('/etc/blackbox_exporter/blackbox_exporter.yml').exists

def test_systemd_unit_exists(host):
    '''Check is systemd unit created'''
    host.file('/etc/systemd/system/blackbox_exporter.service').exists

def test_blackbox_exporter_running(Service):
    '''Check if backbox_exporter service is running'''
    service = Service('blackbox_exporter.service')
    assert service.is_running
    assert service.is_enabled

