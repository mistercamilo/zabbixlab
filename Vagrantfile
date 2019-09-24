# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.define :zabbix do |master|
      master.vm.host_name = "zabbix-server"
      master.vm.network "private_network", ip:"192.168.100.10"
      master.vm.network "forwarded_port", guest: 80, host: 8080
      master.vm.provider :virtualbox do |vb|
          vb.customize ["modifyvm", :id, "--memory", "1024"]
          vb.customize ["modifyvm", :id, "--cpus", "1"]
      end
#      master.vm.provision "shell",
#        inline: "sudo apt update && sudo apt install -y vim curl zabbix-server-mysql zabbix-frontend-php zabbix-agent"
  end

  config.vm.define :client do |master|
    master.vm.host_name = "client"
    master.vm.network "private_network", ip:"192.168.100.20"
    master.vm.network "forwarded_port", guest: 8080, host: 9090
    master.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "512"]
        vb.customize ["modifyvm", :id, "--cpus", "1"]
    end
    master.vm.provision "shell",
      inline: "sudo apt update && sudo apt install -y zabbix-agent zabbix-java-gateway"
  end

end