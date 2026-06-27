Vagrant.configure("2") do |config|
  # Используем Ubuntu 22.04
  config.vm.box = "ubuntu/jammy64"
  
  # Пробрасываем порт 8080 (Windows) -> 5000 (Linux)
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 1
  end

  # Настройка через Ansible
  config.vm.provision "ansible_local" do |ansible|
    # Путь к плейбуку относительно этого Vagrantfile
    ansible.playbook = "ansible/deploy.yml"
    # Vagrant сам попробует установить Ansible внутри виртуалки
    ansible.install = true
  end
end