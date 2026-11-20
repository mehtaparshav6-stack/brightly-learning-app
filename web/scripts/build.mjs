import {context} from 'esbuild';
import {copyFile, mkdir, readFile, rm, writeFile} from 'node:fs/promises';
import {join} from 'node:path';

const watch = process.argv.includes('--watch');
await rm('dist', {recursive:true,force:true});
await mkdir('dist/assets', {recursive:true});
const html = (await readFile('index.html','utf8'))
  .replace('<script type="module" src="/src/main.jsx"></script>', '<link rel="stylesheet" href="/assets/main.css"/><script type="module" src="/assets/main.js"></script>');
await writeFile('dist/index.html', html);
await copyFile('public/favicon.svg','dist/favicon.svg');
const build = await context({entryPoints:['src/main.jsx'],outdir:'dist/assets',entryNames:'[name]',chunkNames:'chunk-[hash]',bundle:true,splitting:true,format:'esm',platform:'browser',target:['es2022'],minify:!watch,sourcemap:watch,logLevel:'info'});
await build.rebuild();
if(watch){await build.watch();console.log('Watching Brightly source. Refresh your browser to see changes.')}else{await build.dispose()}
