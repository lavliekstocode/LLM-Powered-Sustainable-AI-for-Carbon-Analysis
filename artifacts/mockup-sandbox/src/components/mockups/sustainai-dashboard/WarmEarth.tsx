import React, { useState } from 'react';
import { 
  Leaf, 
  BarChart3, 
  Building2, 
  Calculator, 
  Globe, 
  Download,
  Zap,
  Cloud,
  Cpu,
  TreePine,
  Car,
  Smartphone,
  Video,
  Coffee,
  CheckCircle2,
  AlertCircle
} from 'lucide-react';

export function WarmEarth() {
  const [prompt, setPrompt] = useState("");
  const [hasCalculated, setHasCalculated] = useState(false);

  // Mock data
  const metrics = {
    tokens: "3,450",
    energy: "0.0152 Wh",
    co2: "0.0065 g",
    rating: "A+"
  };

  const equivalencies = {
    trees: "0.0003",
    car: "0.025",
    phone: "1.2",
    streaming: "0.5",
    coffee: "0.05"
  };

  const navItems = [
    { name: "Prompt Impact Calculator", icon: Calculator, active: true },
    { name: "Model Emission Comparison", icon: BarChart3, active: false },
    { name: "Company Carbon Dashboards", icon: Building2, active: false },
    { name: "Enterprise Simulator", icon: Zap, active: false },
    { name: "Carbon Equivalency Visualizer", icon: Globe, active: false },
    { name: "Download Reports", icon: Download, active: false },
  ];

  const handleCalculate = () => {
    if (prompt) setHasCalculated(true);
  };

  return (
    <div className="flex h-screen bg-[#FFFBEB] font-sans text-[#44403C]">
      {/* Import Playfair Display */}
      <style dangerouslySetInnerHTML={{__html: `
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');
        .font-playfair { font-family: 'Playfair Display', serif; }
        .paper-shadow { box-shadow: 0 4px 6px -1px rgba(120, 113, 108, 0.1), 0 2px 4px -1px rgba(120, 113, 108, 0.06); }
      `}} />

      {/* Sidebar */}
      <div className="w-72 bg-[#F5F5F4] border-r border-[#E7E5E4] flex flex-col shadow-[1px_0_5px_rgba(0,0,0,0.02)] z-10">
        <div className="p-6">
          <div className="flex items-center gap-3 text-[#65A30D]">
            <Leaf className="w-8 h-8" />
            <h1 className="font-playfair text-2xl font-bold text-[#292524] tracking-tight">SustainAI</h1>
          </div>
          <p className="text-sm text-[#78716C] mt-2 italic font-playfair">AI Carbon Intelligence Dashboard</p>
        </div>

        <div className="px-4 py-2 flex-1">
          <h2 className="text-xs uppercase tracking-widest text-[#A8A29E] font-bold mb-3 px-2">Navigation</h2>
          <nav className="space-y-1">
            {navItems.map((item, i) => (
              <button 
                key={i}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-colors ${
                  item.active 
                    ? 'bg-[#E7E5E4] text-[#292524] font-medium' 
                    : 'text-[#78716C] hover:bg-[#F5F5F4] hover:text-[#292524]'
                }`}
              >
                <item.icon className={`w-4 h-4 ${item.active ? 'text-[#C2410C]' : 'text-[#A8A29E]'}`} />
                {item.name}
              </button>
            ))}
          </nav>
        </div>

        <div className="p-4 border-t border-[#E7E5E4]">
          <h2 className="text-xs uppercase tracking-widest text-[#A8A29E] font-bold mb-3 px-2">Quick Settings</h2>
          <div className="px-2 mb-4">
            <label className="block text-xs text-[#78716C] mb-1.5 font-medium">Default Region</label>
            <select className="w-full bg-[#FAFAF9] border border-[#D6D3D1] rounded-md py-1.5 px-2 text-sm text-[#44403C] focus:outline-none focus:ring-1 focus:ring-[#D97706] focus:border-[#D97706]">
              <option>US East (Virginia)</option>
              <option>EU West (Ireland)</option>
              <option>Asia Pacific (Tokyo)</option>
            </select>
          </div>
        </div>

        <div className="p-4 bg-[#FAFAF9] border-t border-[#E7E5E4]">
          <div className="flex items-start gap-2">
            <AlertCircle className="w-4 h-4 text-[#D97706] shrink-0 mt-0.5" />
            <p className="text-xs text-[#78716C] leading-relaxed">
              SustainAI helps you understand and reduce the environmental impact of AI usage. Calculate emissions, compare models, and get personalized recommendations.
            </p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto">
        <div className="max-w-6xl mx-auto p-10">
          <header className="mb-10">
            <h1 className="font-playfair text-4xl font-bold text-[#292524] mb-3">Prompt Impact Calculator</h1>
            <p className="text-[#57534E] text-lg max-w-2xl">
              Calculate the environmental impact of your AI queries in real-time. Understand the footprint of your specific use cases.
            </p>
          </header>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-10">
            <div className="lg:col-span-2 space-y-4">
              <label className="block font-medium text-[#44403C]">Enter your prompt</label>
              <textarea 
                className="w-full h-40 bg-white border border-[#D6D3D1] rounded-xl p-4 text-[#44403C] focus:outline-none focus:ring-2 focus:ring-[#D97706]/50 focus:border-[#D97706] paper-shadow resize-none"
                placeholder="Type or paste your AI prompt here to analyze its environmental impact..."
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
              />
            </div>
            
            <div className="space-y-6">
              <div className="bg-[#F5F5F4] p-5 rounded-xl border border-[#E7E5E4] paper-shadow">
                <h3 className="font-playfair text-lg font-bold text-[#292524] mb-4">Configuration</h3>
                
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-[#57534E] mb-1.5">Select AI Model</label>
                    <select className="w-full bg-white border border-[#D6D3D1] rounded-lg py-2 px-3 text-[#44403C] focus:outline-none focus:ring-1 focus:ring-[#D97706] focus:border-[#D97706]">
                      <option>GPT-4o (OpenAI)</option>
                      <option>Claude 3.5 Sonnet (Anthropic)</option>
                      <option>Gemini 1.5 Pro (Google)</option>
                      <option>Llama 3 70B (Meta)</option>
                    </select>
                  </div>
                  
                  <div>
                    <label className="block text-sm font-medium text-[#57534E] mb-1.5">Processing Region</label>
                    <select className="w-full bg-white border border-[#D6D3D1] rounded-lg py-2 px-3 text-[#44403C] focus:outline-none focus:ring-1 focus:ring-[#D97706] focus:border-[#D97706]">
                      <option>US West (Oregon) - 78% Renewable</option>
                      <option>EU North (Sweden) - 98% Renewable</option>
                      <option>Asia (Singapore) - 45% Renewable</option>
                    </select>
                  </div>

                  <div className="flex items-center gap-2 pt-2">
                    <input type="checkbox" id="include-response" className="rounded border-[#D6D3D1] text-[#C2410C] focus:ring-[#D97706]" defaultChecked />
                    <label htmlFor="include-response" className="text-sm text-[#57534E]">Include estimated response tokens</label>
                  </div>
                </div>
              </div>

              <button 
                onClick={handleCalculate}
                className="w-full bg-[#C2410C] hover:bg-[#9A3412] text-white font-medium py-3.5 px-4 rounded-xl shadow-lg transition-all transform active:scale-[0.98] flex items-center justify-center gap-2"
              >
                <Calculator className="w-5 h-5" />
                Calculate Impact
              </button>
            </div>
          </div>

          {hasCalculated && (
            <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
              <div className="flex items-center gap-3 mb-6">
                <h2 className="font-playfair text-2xl font-bold text-[#292524]">Impact Results</h2>
                <div className="h-px bg-[#D6D3D1] flex-1"></div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-10">
                <MetricCard 
                  title="Total Tokens" 
                  value={metrics.tokens} 
                  subtext="1,200 prompt + 2,250 response" 
                  icon={Cpu}
                  color="text-[#0284C7]" 
                  bg="bg-[#E0F2FE]"
                />
                <MetricCard 
                  title="Energy Used" 
                  value={metrics.energy} 
                  subtext="0.000015 kWh" 
                  icon={Zap}
                  color="text-[#D97706]" 
                  bg="bg-[#FEF3C7]"
                />
                <MetricCard 
                  title="CO₂ Emitted" 
                  value={metrics.co2} 
                  subtext="0.000006 kg" 
                  icon={Cloud}
                  color="text-[#65A30D]" 
                  bg="bg-[#ECFCCB]"
                />
                <MetricCard 
                  title="Efficiency Rating" 
                  value={metrics.rating} 
                  subtext="Model Efficiency" 
                  icon={CheckCircle2}
                  color="text-[#059669]" 
                  bg="bg-[#D1FAE5]"
                />
              </div>

              <div className="flex items-center gap-3 mb-6">
                <h2 className="font-playfair text-2xl font-bold text-[#292524]">Environmental Equivalencies</h2>
                <div className="h-px bg-[#D6D3D1] flex-1"></div>
              </div>

              <div className="bg-white rounded-xl border border-[#E7E5E4] p-8 paper-shadow">
                <div className="grid grid-cols-2 md:grid-cols-5 gap-8">
                  <EquivalencyItem icon={TreePine} value={equivalencies.trees} label="Trees needed" sublabel="for 1 year" />
                  <EquivalencyItem icon={Car} value={`${equivalencies.car} km`} label="Car Distance" sublabel="of driving" />
                  <EquivalencyItem icon={Smartphone} value={equivalencies.phone} label="Phone Charges" sublabel="full charges" />
                  <EquivalencyItem icon={Video} value={`${equivalencies.streaming} hrs`} label="Streaming" sublabel="of HD video" />
                  <EquivalencyItem icon={Coffee} value={equivalencies.coffee} label="Coffee" sublabel="cups of coffee" />
                </div>
              </div>

              <div className="mt-8 text-center">
                <button className="text-[#C2410C] hover:text-[#9A3412] font-medium text-sm inline-flex items-center gap-1.5 border border-[#C2410C] rounded-full px-4 py-2 hover:bg-[#FFF7ED] transition-colors">
                  View Detailed LLM Explanation
                </button>
              </div>
            </div>
          )}
          
          {!hasCalculated && (
            <div className="bg-[#F5F5F4] border border-[#E7E5E4] border-dashed rounded-xl p-12 text-center">
              <Leaf className="w-12 h-12 text-[#A8A29E] mx-auto mb-4 opacity-50" />
              <h3 className="font-playfair text-xl text-[#78716C] font-medium mb-2">Ready to Calculate</h3>
              <p className="text-[#A8A29E] max-w-sm mx-auto">Enter a prompt above and click calculate to see the environmental impact of your AI usage.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function MetricCard({ title, value, subtext, icon: Icon, color, bg }: any) {
  return (
    <div className="bg-white rounded-xl p-5 border border-[#E7E5E4] border-b-4 border-b-[#D6D3D1] paper-shadow relative overflow-hidden group">
      <div className={`absolute top-0 right-0 w-24 h-24 rounded-bl-full ${bg} opacity-50 -z-0 transition-transform group-hover:scale-110`}></div>
      <div className="relative z-10">
        <div className="flex justify-between items-start mb-4">
          <h3 className="text-sm font-medium text-[#78716C]">{title}</h3>
          <div className={`${bg} ${color} p-2 rounded-lg`}>
            <Icon className="w-4 h-4" />
          </div>
        </div>
        <div className="font-playfair text-3xl font-bold text-[#292524] mb-1">{value}</div>
        <div className="text-xs text-[#A8A29E]">{subtext}</div>
      </div>
    </div>
  );
}

function EquivalencyItem({ icon: Icon, value, label, sublabel }: any) {
  return (
    <div className="flex flex-col items-center text-center group">
      <div className="w-14 h-14 bg-[#FAFAF9] border border-[#E7E5E4] rounded-full flex items-center justify-center mb-4 group-hover:border-[#C2410C] group-hover:bg-[#FFF7ED] transition-colors duration-300">
        <Icon className="w-6 h-6 text-[#78716C] group-hover:text-[#C2410C] transition-colors" />
      </div>
      <div className="font-playfair text-xl font-bold text-[#292524] mb-1">{value}</div>
      <div className="text-sm font-medium text-[#57534E]">{label}</div>
      <div className="text-xs text-[#A8A29E] mt-0.5">{sublabel}</div>
    </div>
  );
}
