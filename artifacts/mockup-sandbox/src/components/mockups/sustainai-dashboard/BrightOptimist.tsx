import React, { useState } from "react";
import { 
  Calculator, 
  BarChart3, 
  Building2, 
  Globe2, 
  Download, 
  Leaf,
  Info,
  ChevronDown,
  Sparkles,
  Zap,
  Cloud,
  Award,
  TreePine,
  Car,
  Smartphone,
  Tv,
  Coffee
} from "lucide-react";

export function BrightOptimist() {
  const [prompt, setPrompt] = useState("");
  const [calculating, setCalculating] = useState(false);
  const [showResults, setShowResults] = useState(true);

  const handleCalculate = () => {
    setCalculating(true);
    setTimeout(() => {
      setCalculating(false);
      setShowResults(true);
    }, 800);
  };

  return (
    <div className="flex h-screen w-full bg-[#F8FAFC] text-slate-800 font-sans overflow-hidden">
      
      {/* Sidebar */}
      <aside className="w-72 bg-white border-r border-slate-100 flex flex-col justify-between flex-shrink-0 shadow-[4px_0_24px_rgba(0,0,0,0.02)] z-10">
        <div>
          <div className="p-8 flex items-center gap-3">
            <div className="bg-gradient-to-br from-lime-400 to-emerald-500 p-2.5 rounded-2xl shadow-lg shadow-lime-200">
              <Leaf className="w-7 h-7 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-black tracking-tight text-slate-900 leading-none">SustainAI</h1>
              <p className="text-xs font-semibold text-emerald-500 mt-1 uppercase tracking-wider">Carbon Intelligence</p>
            </div>
          </div>

          <nav className="px-4 space-y-1.5 mt-2">
            <NavItem icon={<Calculator className="w-5 h-5 text-lime-500" />} label="Prompt Impact" active />
            <NavItem icon={<BarChart3 className="w-5 h-5 text-sky-500" />} label="Model Comparison" />
            <NavItem icon={<Building2 className="w-5 h-5 text-violet-500" />} label="Company Dashboards" />
            <NavItem icon={<Sparkles className="w-5 h-5 text-rose-500" />} label="Enterprise Simulator" />
            <NavItem icon={<Globe2 className="w-5 h-5 text-amber-500" />} label="Carbon Equivalency" />
            <NavItem icon={<Download className="w-5 h-5 text-teal-500" />} label="Download Reports" />
          </nav>
        </div>

        <div className="p-6 space-y-6">
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-400 uppercase tracking-wider pl-1">Default Region</label>
            <div className="relative">
              <select className="w-full appearance-none bg-slate-50 border-2 border-slate-100 rounded-xl px-4 py-3 pr-10 text-sm font-semibold text-slate-700 focus:outline-none focus:border-lime-400 focus:ring-4 focus:ring-lime-100 transition-all cursor-pointer">
                <option>Global Average</option>
                <option>US West (Oregon)</option>
                <option>EU Central (Frankfurt)</option>
                <option>Asia Pacific (Tokyo)</option>
              </select>
              <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400 pointer-events-none" />
            </div>
          </div>

          <div className="bg-sky-50 rounded-2xl p-5 border border-sky-100 relative overflow-hidden group cursor-pointer hover:bg-sky-100 transition-colors">
            <div className="absolute top-0 right-0 p-3 opacity-20 group-hover:opacity-30 transition-opacity">
              <Info className="w-16 h-16 text-sky-500 -mr-4 -mt-4" />
            </div>
            <div className="flex items-center gap-2 mb-2 relative z-10">
              <Info className="w-5 h-5 text-sky-500" />
              <h3 className="font-bold text-sky-900">About</h3>
            </div>
            <p className="text-sm text-sky-700 leading-relaxed relative z-10 font-medium">
              SustainAI helps you understand and reduce the environmental impact of AI usage.
            </p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto bg-[#F8FAFC]">
        <div className="max-w-5xl mx-auto p-10 pb-20">
          
          <header className="mb-10">
            <h2 className="text-4xl font-black text-slate-900 mb-3 tracking-tight">Prompt Impact Calculator <span className="inline-block animate-bounce ml-2">✨</span></h2>
            <p className="text-lg text-slate-500 font-medium max-w-2xl leading-relaxed">
              Calculate the environmental footprint of your AI queries in real-time. Make every token count!
            </p>
          </header>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-10">
            <div className="lg:col-span-2">
              <div className="bg-white rounded-[2rem] p-6 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100">
                <label className="block text-sm font-bold text-slate-700 mb-3 ml-2">Enter your prompt</label>
                <textarea 
                  className="w-full bg-slate-50 border-2 border-slate-100 rounded-2xl p-5 text-slate-700 min-h-[160px] focus:outline-none focus:border-violet-400 focus:ring-4 focus:ring-violet-100 transition-all font-medium text-lg placeholder:text-slate-300 resize-none"
                  placeholder="Write a python script to analyze customer churn data..."
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                />
              </div>
            </div>

            <div className="space-y-5">
              <div className="bg-white rounded-[2rem] p-6 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100">
                <div className="space-y-5">
                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2 ml-2">AI Model</label>
                    <div className="relative">
                      <select className="w-full appearance-none bg-slate-50 border-2 border-slate-100 rounded-xl px-4 py-3 pr-10 text-sm font-semibold text-slate-700 focus:outline-none focus:border-rose-400 focus:ring-4 focus:ring-rose-100 transition-all cursor-pointer">
                        <option>GPT-4 (OpenAI)</option>
                        <option>Claude 3 Opus (Anthropic)</option>
                        <option>Gemini 1.5 Pro (Google)</option>
                        <option>Llama 3 70B (Meta)</option>
                      </select>
                      <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400 pointer-events-none" />
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-bold text-slate-700 mb-2 ml-2">Processing Region</label>
                    <div className="relative">
                      <select className="w-full appearance-none bg-slate-50 border-2 border-slate-100 rounded-xl px-4 py-3 pr-10 text-sm font-semibold text-slate-700 focus:outline-none focus:border-amber-400 focus:ring-4 focus:ring-amber-100 transition-all cursor-pointer">
                        <option>US West (Oregon)</option>
                        <option>US East (N. Virginia)</option>
                        <option>EU West (Ireland)</option>
                      </select>
                      <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400 pointer-events-none" />
                    </div>
                  </div>
                  
                  <label className="flex items-center gap-3 cursor-pointer group mt-2">
                    <div className="relative flex items-center justify-center w-6 h-6 bg-lime-100 rounded-md border-2 border-lime-500 group-hover:bg-lime-200 transition-colors">
                      <div className="w-3 h-3 bg-lime-500 rounded-sm"></div>
                    </div>
                    <span className="text-sm font-bold text-slate-600">Include estimated response</span>
                  </label>
                </div>
              </div>

              <button 
                onClick={handleCalculate}
                className="w-full bg-gradient-to-r from-lime-400 via-emerald-400 to-teal-400 text-white font-bold text-lg py-4 rounded-2xl shadow-[0_8px_20px_rgba(16,185,129,0.3)] hover:shadow-[0_12px_25px_rgba(16,185,129,0.4)] hover:-translate-y-1 transition-all flex items-center justify-center gap-2"
              >
                {calculating ? (
                  <span className="animate-pulse flex items-center gap-2">Calculating Magic... ✨</span>
                ) : (
                  <>Calculate Impact <Sparkles className="w-5 h-5" /></>
                )}
              </button>
            </div>
          </div>

          {showResults && (
            <div className="animate-in fade-in slide-in-from-bottom-8 duration-700 ease-out">
              <div className="flex items-center gap-4 mb-6">
                <div className="h-px bg-slate-200 flex-1"></div>
                <h3 className="text-xl font-black text-slate-400 tracking-wider uppercase">Your Impact Dashboard</h3>
                <div className="h-px bg-slate-200 flex-1"></div>
              </div>

              {/* Metric Cards */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mb-10">
                <MetricCard 
                  title="Total Tokens" 
                  value="1,245" 
                  subtitle="325 prompt + 920 response"
                  icon={<Zap className="w-6 h-6 text-white" />}
                  gradient="from-amber-400 to-orange-500"
                  shadowColor="rgba(245, 158, 11, 0.3)"
                />
                <MetricCard 
                  title="Energy Used" 
                  value="0.0034 Wh" 
                  subtitle="0.000003 kWh"
                  icon={<Zap className="w-6 h-6 text-white" />}
                  gradient="from-sky-400 to-blue-500"
                  shadowColor="rgba(14, 165, 233, 0.3)"
                />
                <MetricCard 
                  title="CO₂ Emitted" 
                  value="1.24 g" 
                  subtitle="0.00124 kg"
                  icon={<Cloud className="w-6 h-6 text-white" />}
                  gradient="from-violet-400 to-purple-500"
                  shadowColor="rgba(139, 92, 246, 0.3)"
                />
                <MetricCard 
                  title="Efficiency" 
                  value="A-" 
                  subtitle="Model Efficiency Rating"
                  icon={<Award className="w-6 h-6 text-white" />}
                  gradient="from-lime-400 to-emerald-500"
                  shadowColor="rgba(132, 204, 22, 0.3)"
                />
              </div>

              {/* Equivalencies */}
              <div className="bg-white rounded-[2rem] p-8 shadow-[0_8px_30px_rgb(0,0,0,0.04)] border border-slate-100">
                <h3 className="text-xl font-black text-slate-800 mb-8 flex items-center gap-3">
                  <span className="bg-rose-100 text-rose-500 p-2 rounded-xl"><Globe2 className="w-5 h-5" /></span>
                  What does this mean in the real world?
                </h3>
                
                <div className="grid grid-cols-2 md:grid-cols-5 gap-6">
                  <EquivalencyItem icon={<TreePine className="w-8 h-8 text-emerald-500" />} value="0.0001" label="Trees needed" color="bg-emerald-50" textColor="text-emerald-600" />
                  <EquivalencyItem icon={<Car className="w-8 h-8 text-sky-500" />} value="0.005 km" label="Driving" color="bg-sky-50" textColor="text-sky-600" />
                  <EquivalencyItem icon={<Smartphone className="w-8 h-8 text-violet-500" />} value="0.15" label="Phone charges" color="bg-violet-50" textColor="text-violet-600" />
                  <EquivalencyItem icon={<Tv className="w-8 h-8 text-rose-500" />} value="0.02 hrs" label="Video streaming" color="bg-rose-50" textColor="text-rose-600" />
                  <EquivalencyItem icon={<Coffee className="w-8 h-8 text-amber-500" />} value="0.04" label="Cups of coffee" color="bg-amber-50" textColor="text-amber-600" />
                </div>
              </div>

            </div>
          )}
        </div>
      </main>
    </div>
  );
}

function NavItem({ icon, label, active = false }: { icon: React.ReactNode, label: string, active?: boolean }) {
  return (
    <div className={`flex items-center gap-3 px-4 py-3.5 rounded-2xl cursor-pointer transition-all ${
      active 
        ? "bg-slate-50 font-bold text-slate-900 shadow-sm border border-slate-100" 
        : "text-slate-500 font-semibold hover:bg-slate-50/50 hover:text-slate-700"
    }`}>
      <div className={`${active ? 'scale-110 transition-transform' : ''}`}>
        {icon}
      </div>
      <span>{label}</span>
    </div>
  );
}

function MetricCard({ title, value, subtitle, icon, gradient, shadowColor }: { title: string, value: string, subtitle: string, icon: React.ReactNode, gradient: string, shadowColor: string }) {
  return (
    <div className={`bg-gradient-to-br ${gradient} rounded-[2rem] p-6 text-white relative overflow-hidden group hover:-translate-y-1 transition-transform duration-300`} style={{ boxShadow: `0 12px 24px ${shadowColor}` }}>
      <div className="absolute -right-6 -top-6 w-24 h-24 bg-white opacity-10 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-500"></div>
      
      <div className="flex justify-between items-start mb-4 relative z-10">
        <h4 className="font-bold text-white/90 text-sm tracking-wide uppercase">{title}</h4>
        <div className="bg-white/20 p-2 rounded-xl backdrop-blur-md">
          {icon}
        </div>
      </div>
      
      <div className="relative z-10">
        <div className="text-3xl font-black mb-1 tracking-tight">{value}</div>
        <div className="text-sm font-semibold text-white/80">{subtitle}</div>
      </div>
    </div>
  );
}

function EquivalencyItem({ icon, value, label, color, textColor }: { icon: React.ReactNode, value: string, label: string, color: string, textColor: string }) {
  return (
    <div className="flex flex-col items-center text-center group cursor-default">
      <div className={`w-16 h-16 ${color} rounded-2xl flex items-center justify-center mb-4 group-hover:-translate-y-2 group-hover:shadow-lg transition-all duration-300`}>
        {icon}
      </div>
      <div className={`text-xl font-black ${textColor} mb-1`}>{value}</div>
      <div className="text-sm font-semibold text-slate-500">{label}</div>
    </div>
  );
}
