import React, {useEffect,useRef,useState} from 'react';
import {Canvas, useFrame} from '@react-three/fiber';

function Seed({position,color,scale=1,phase=0}) {
  const ref=useRef();
  useFrame(({clock,pointer})=>{if(!ref.current)return;const t=clock.getElapsedTime();ref.current.rotation.y=pointer.x*.14+Math.sin(t*.45+phase)*.08;ref.current.position.y=position[1]+Math.sin(t*.7+phase)*.09});
  return <group ref={ref} position={position} scale={scale}>
    <mesh rotation={[0,0,.43]} position={[0,.08,0]} castShadow><sphereGeometry args={[.62,32,24]}/><meshStandardMaterial color={color} roughness={.54}/></mesh>
    <mesh position={[0,-.64,.1]} castShadow><cylinderGeometry args={[.1,.16,.95,16]}/><meshStandardMaterial color="#5bc7a3" roughness={.7}/></mesh>
    <mesh position={[-.3,-.48,.1]} rotation={[0,0,.54]} castShadow><sphereGeometry args={[.31,18,14]}/><meshStandardMaterial color="#7bdcb6" roughness={.8}/></mesh>
    <mesh position={[.28,-.7,.06]} rotation={[0,0,-.5]} castShadow><sphereGeometry args={[.26,18,14]}/><meshStandardMaterial color="#89e2c1" roughness={.8}/></mesh>
  </group>
}
function Scene({scroll}){
  const arch=useRef();
  useFrame(({clock,pointer},delta)=>{if(arch.current){const progress=Math.min(1,scroll.current/(window.innerHeight*.75));const ease=1-Math.exp(-delta*3);arch.current.rotation.y+=(pointer.x*.16+Math.sin(clock.getElapsedTime()*.22)*.08+progress*.16-arch.current.rotation.y)*ease;arch.current.rotation.x+=(-pointer.y*.06+progress*.08-arch.current.rotation.x)*ease;arch.current.position.y+=(-.18+progress*.52-arch.current.position.y)*ease;arch.current.scale.setScalar(1-progress*.1)} });
  return <>
    <ambientLight intensity={2.1}/><directionalLight position={[-5,8,8]} intensity={3} color="#fff5d8"/>
    <pointLight position={[5,1,3]} intensity={45} color="#ffdbba"/>
    <group ref={arch} position={[.35,-.18,0]}>
      <mesh position={[0,.1,-.8]} rotation={[0,0,0]}><torusGeometry args={[2.27,.28,20,90,Math.PI]}/><meshStandardMaterial color="#ffb5c1" roughness={.43}/></mesh>
      <mesh position={[-2.27,-1.05,-.8]}><cylinderGeometry args={[.28,.28,2.35,24]}/><meshStandardMaterial color="#ffb5c1" roughness={.43}/></mesh>
      <mesh position={[2.27,-1.05,-.8]}><cylinderGeometry args={[.28,.28,2.35,24]}/><meshStandardMaterial color="#ffb5c1" roughness={.43}/></mesh>
      <mesh position={[.15,-2.19,-.2]} scale={[2.6,.18,1.45]}><sphereGeometry args={[1,40,20]}/><meshStandardMaterial color="#6bcbae" roughness={.9}/></mesh>
      <Seed position={[-1.15,-.92,.65]} color="#ffe388" scale={.82}/>
      <Seed position={[.2,-.55,1]} color="#ffa4ae" scale={1.15} phase={1.3}/>
      <Seed position={[1.36,-1.05,.45]} color="#c7b1ff" scale={.72} phase={2.6}/>
      <mesh position={[-.35,1.96,.32]}><sphereGeometry args={[.24,24,16]}/><meshStandardMaterial color="#ffec9d" emissive="#ffdf7c" emissiveIntensity={.25}/></mesh>
      <mesh position={[1.63,1.4,.1]} scale={[.14,.14,.14]}><octahedronGeometry/><meshStandardMaterial color="#fef1b2"/></mesh>
      <mesh position={[-1.8,.95,.45]} scale={[.1,.1,.1]}><octahedronGeometry/><meshStandardMaterial color="#fef1b2"/></mesh>
    </group>
  </>
}
export default function Garden(){
  const scroll=useRef(0),container=useRef(null),[visible,setVisible]=useState(true),[reduced,setReduced]=useState(()=>window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  useEffect(()=>{const onScroll=()=>{scroll.current=window.scrollY};onScroll();window.addEventListener('scroll',onScroll,{passive:true});const observer=new IntersectionObserver(([entry])=>setVisible(entry.isIntersecting),{threshold:0});if(container.current)observer.observe(container.current);const media=window.matchMedia('(prefers-reduced-motion: reduce)');const onMedia=()=>setReduced(media.matches);media.addEventListener('change',onMedia);return()=>{window.removeEventListener('scroll',onScroll);observer.disconnect();media.removeEventListener('change',onMedia)}},[]);
  return <div ref={container} className="garden-canvas" role="img" aria-label="A floating pastel garden with an arch and three growing flowers">{reduced?<div className="garden-fallback">✿</div>:<Canvas frameloop={visible?'always':'never'} dpr={[1,1.5]} shadows camera={{position:[0,0,8],fov:44}} gl={{alpha:true,antialias:true}}><Scene scroll={scroll}/></Canvas>}</div>
}
