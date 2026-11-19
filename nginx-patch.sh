#!/bin/bash -xe

# runs on the unifi device at boot
# place this file in /data/on_boot.d/ (create if necessary)
# see https://github.com/unifi-utilities/unifi-common

# create the patch file

cat <<EOF > /tmp/nginx.conf-patch
--- /etc/nginx/nginx.conf	2026-11-18 20:47:42.795431791 -0500
+++ /tmp/nginx.conf-patch	2026-11-18 20:56:18.637581798 -0500
@@ -127,4 +127,8 @@
     include /data/unifi-core/config/http/upstream-*.conf;

     include /data/unifi-core/config/http/site-*.conf;
+
+    # MCHP local includes
+    include /etc/nginx/conf.d/*.conf;
+
 }
EOF

# check if the patch already exists

grep MCHP /etc/nginx/nginx.conf || patch --verbose /etc/nginx/nginx.conf </tmp/nginx.conf-patch

patch_status=$?

echo $patch_status

curl -s -O --output-dir /etc/nginx/conf.d/ https://raw.githubusercontent.com/puskar/odds_ends/HEAD/byramcrest.org.conf
curl -s -O --output-dir /etc/nginx/conf.d/ https://raw.githubusercontent.com/puskar/odds_ends/HEAD/api.puskar.net.conf

nginx -t

config_status=$?

echo $config_status

# patch is applied and config checks out, so restart nginx

if [[ "$patch_status" -eq 0 && "$config_status" -eq 0 ]]; then
    systemctl restart nginx
fi

