import React from 'react';
import Header from '../components/Header';
import Hero from '../components/Hero';
import CodeDemo from '../components/CodeDemo';
import Features from '../components/Features';
import Process from '../components/Process';
import Pricing from '../components/Pricing';

import Footer from '../components/Footer';

function Landing(){
    return (
        <div>
           <Header />
           <Hero />
           <CodeDemo />
           <Features />
           <Process />
           <Pricing />
           <Footer />
        </div>
    )
}

export default Landing;