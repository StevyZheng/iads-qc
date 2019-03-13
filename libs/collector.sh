#! /bin/bash

log_path="/tmp/logfiles"
proc_path=${log_path}/proc
etc_path=${log_path}/etc

mkdir -p ${log_path}
mkdir -p ${log_path}/var_log
mkdir -p ${proc_path}
mkdir -p ${etc_path}

uname -a >> ${log_path}/uname_a
\cp /etc/redhat_release ${log_path}/

\cp -arf /var/log/* ${log_path}/var_log/
\cp -arf /var/carsh ${log_path}
\cp -arf /proc/iomem ${proc_path}
\cp -arf /proc/cpuinfo ${proc_path}
\cp -arf /proc/devices ${proc_path}
\cp -arf /proc/opports ${proc_path}
\cp -arf /proc/meminfo ${proc_path}
\cp -arf /proc/modules ${proc_path}

lspci -xxxvvv >> ${log_path}/lspci.log
lsscsi -tg >> ${log_path}/lsscsi.log
route -n >> ${log_path}/route.log
netstat -rn >> ${log_path}/netstat.log

\cp -arf /etc/hosts ${etc_path}
\cp -arf /etc/resolv.conf ${etc_path}
\cp -arf /etc/nsswitch.conf ${etc_path}

ip addr show >> ${log_path}/ip_addr.log
ip route show >> ${log_path}/ip_route.log
who >> ${log_path}/who.log
ps -aux >> ${log_path}/ps_aux.log
ps -AL >> ${log_path}/ps_AL.log
yum list installed >> ${log_path}/yum_list.log
rpm -qa|grep lustre >> ${log_path}/lustre.ver
rpm -qa|grep zfs >> ${log_path}/zfs.ver
rpm -qa|grep spl >> ${log_path}/spl_ver
lsmod >> ${log_path}/lsmod.log
dkms status >> ${log_path}/dkms.log
zpool status >> ${log_path}/zpool_status
zpool status -v >> ${log_path}/zpool_status_v
zpool list >> ${log_path}/zpool_list
mount >> ${log_path}/mount.log
lctl dl >> ${log_path}/lctl.log
lsblk >> ${log_path}/lsblk.log
service multipathd status >> ${log_path}/multipathd.log
\cp -arf /etc/multipath.conf >> ${etc_path}/
df -h >> ${log_path}/df.log
dmesg >> ${log_path}/dmesg.log

sestatus >> ${log_path}/selinux_status

for i in /dev/sd*
do
    smartctl --all ${i} >> ${log_path}/smart_sd${i}.log
done

cd /tmp
tar czvf log.tgz ${log_path}











