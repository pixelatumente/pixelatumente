# pixelatumente-2 — reglas del proyecto

## Reglas de edición (aplican a cualquier agente que trabaje aquí)

1. **Cambios quirúrgicos**: toca solo lo que pide la tarea. No refactorices código adyacente, no reformatees archivos no relacionados, no borres código muerto (menciónalo y sigue).
2. **Menciona, no arregles**: si ves un problema fuera del alcance, avísalo en el resumen final, no lo toques.
3. **Confirma antes de >3 archivos**: si la tarea implica editar más de 3 archivos o cambiar diseño/estructura, expón el plan y espera confirmación.
4. **Criterio de éxito**: antes de empezar, define cómo se verifica que la tarea quedó bien (build, tests, deploy) y verifícalo al terminar.
5. **Piensa antes de codificar**: si la petición es ambigua, pregunta (opciones A/B) en vez de asumir.
6. **Simplicidad**: la solución más simple que cumpla el objetivo; sin abstracciones especulativas.

## Datos del proyecto

- pixelatumente.es 2.0 · Astro 7 · **desde 23-sep-2026 servido en el VPS HostUp (136.148.218.48), ya NO en Cloudflare Pages**
- DNS: zona en Cloudflare (NS), apex/www = A a 136.148.218.48 en **nube gris (DNS only)**. Backup de los registros previos al corte: `cf-dns-backup.json` (este repo).
- SSL: certbot **webroot** `/var/www/acme` (`certbot certonly --webroot -w /var/www/acme -d pixelatumente.es -d www.pixelatumente.es`); renovación automática probada con dry-run.
- Config nginx: fuente versionada en `nginx-pixelatumente.conf` (copia viva en `/etc/nginx/sites-available/pixelatumente`). Antes de cada reload: `/usr/local/sbin/check-nginx-conflicts.sh` + `nginx -t`. No editar la copia viva a mano.

### Deploy (build local → VPS)

```bash
cd ~/projects/pixelatumente-2
npm run build
find dist -type f ! -perm -004 -exec chmod 644 {} +   # robots/ads no pueden quedar 600
rsync -az --delete -e "ssh -i ~/.ssh/id_rsa_openssh" dist/ root@136.148.218.48:/var/www/pixelatumente.es/dist/
# verificar: find dist -type f | wc -l debe cuadrar con el del VPS (24 tras la migración)
```

NO hay que tocar nginx en deploys normales (solo cambia si cambian bloques/redirects). El antiguo `wrangler pages deploy dist --project-name pixelatumente` ya no se usa.

### Rollback a Cloudflare Pages

1. Restaurar desde `cf-dns-backup.json` los CNAME apex y www → `pixelatumente.pages.dev` con `proxied: true` (borrar antes las A).
2. Re-vincular los dominios al proyecto Pages (`POST /accounts/{acc}/pages/projects/pixelatumente/domains/<dominio>` — se borraron al cerrar la migración).
3. `https://pixelatumente.pages.dev/` queda siempre vivo como red de comprobación.
