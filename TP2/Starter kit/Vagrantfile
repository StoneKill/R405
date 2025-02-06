# -*- mode: ruby -*-
# # vi: set ft=ruby :

$subnet = "192.168.57"
$num_dns = 1 #max 9
$num_web = 1 #max 9

Vagrant.configure("2") do |config|

  config.vm.box = "generic/debian11"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 1
    vb.memory = 512
    vb.customize ["modifyvm", :id, "--vram", "8"] # ubuntu defaults to 256 MB which is a waste of precious RAM
    vb.linked_clone = true
  end

  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end

  config.vm.define "lb-1" do |node|
    node.vm.hostname = "LB-1.lab.lan"
    ip = "#{$subnet}.#{101}"
    node.vm.network :private_network, ip: ip
    node.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
  end
  
  (1..$num_dns).each do |i|
    config.vm.define "dns-#{i}" do |node|
      node.vm.hostname = "DNS-#{i}.lab.lan"
      ip = "#{$subnet}.#{i+110}"
      node.vm.network :private_network, ip: ip
    end
  end

  (1..$num_web).each do |i|
    config.vm.define "web-#{i}" do |node|
      node.vm.hostname = "WEB-#{i}.lab.lan" 
      ip = "#{$subnet}.#{i+120}"
      node.vm.network :private_network, ip: ip
    end
  end

end