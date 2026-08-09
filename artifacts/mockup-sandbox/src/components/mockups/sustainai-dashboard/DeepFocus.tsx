import React, { useState } from "react";
import {
  Activity,
  BarChart3,
  Battery,
  Building2,
  Calculator,
  Car,
  ChevronDown,
  CloudLightning,
  Coffee,
  Database,
  Download,
  Flame,
  Globe,
  Info,
  Leaf,
  MonitorPlay,
  Settings,
  Smartphone,
  Trees,
  Zap,
} from "lucide-react";
import { cn } from "@/lib/utils";

export function DeepFocus() {
  const [prompt, setPrompt] = useState(
    "Analyze the Q3 financial reports and generate a comprehensive summary of key performance indicators, market trends, and competitive positioning for the upcoming board meeting."
  );
  const [isCalculated, setIsCalculated] = useState(true);

  const navItems = [
    { name: "Prompt Impact Calculator", icon: Calculator, active: true },
    { name: "Model Emission Comparison", icon: BarChart3 },
    { name: "Company Carbon Dashboards", icon: Building2 },
    { name: "Enterprise Simulator", icon: Database },
    { name: "Carbon Equivalency Visualizer", icon: Globe },
    { name: "Download Reports", icon: Download },
  ];

  const models = [
    "GPT-4 (OpenAI)",
    "GPT-3.5-Turbo (OpenAI)",
    "Claude 3 Opus (Anthropic)",
    "Claude 3 Sonnet (Anthropic)",
    "Gemini 1.5 Pro (Google)",
  ];

  const regions = ["US East (N. Virginia)", "US West (Oregon)", "EU (Frankfurt)", "Asia Pacific (Tokyo)"];

  return (
    <div className="flex h-screen w-full bg-[#0F172A] text-slate-300 font-sans selection:bg-cyan-900 selection:text-cyan-50 overflow-hidden">
      {/* Sidebar */}
      <aside className="w-72 bg-[#020617] border-r border-slate-800 flex flex-col justify-between shrink-0">
        <div>
          <div className="p-6 flex items-center gap-3 border-b border-slate-800/60">
            <div className="h-8 w-8 rounded bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center">
              <Leaf className="h-5 w-5 text-cyan-400" />
            </div>
            <div>
              <h1 className="text-slate-100 font-semibold tracking-tight text-lg">SustainAI</h1>
              <p className="text-xs text-slate-500 font-mono tracking-wider uppercase">Carbon Intel</p>
            </div>
          </div>

          <div className="px-4 py-6 space-y-1">
            <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3 px-2">Navigation</div>
            {navItems.map((item) => (
              <button
                key={item.name}
                className={cn(
                  "w-full flex items-center gap-3 px-3 py-2.5 rounded-md text-sm font-medium transition-all duration-200",
                  item.active
                    ? "bg-blue-900/20 text-blue-400 border border-blue-800/30"
                    : "text-slate-400 hover:text-slate-200 hover:bg-slate-800/50"
                )}
              >
                <item.icon className={cn("h-4 w-4", item.active ? "text-blue-400" : "text-slate-500")} />
                {item.name}
              </button>
            ))}
          </div>
        </div>

        <div className="p-4 space-y-4 border-t border-slate-800/60">
          <div className="space-y-2">
            <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider px-1">Default Region</label>
            <div className="relative">
              <select className="w-full appearance-none bg-slate-900 border border-slate-700 rounded text-sm py-2 pl-3 pr-8 text-slate-300 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500">
                {regions.map((r) => (
                  <option key={r}>{r}</option>
                ))}
              </select>
              <ChevronDown className="absolute right-2.5 top-2.5 h-4 w-4 text-slate-500 pointer-events-none" />
            </div>
          </div>

          <div className="bg-slate-900/50 border border-slate-800 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Info className="h-4 w-4 text-slate-400" />
              <span className="text-xs font-semibold text-slate-300">About SustainAI</span>
            </div>
            <p className="text-xs text-slate-500 leading-relaxed">
              Analyze, simulate, and reduce the environmental impact of your AI infrastructure through data-driven insights.
            </p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-full overflow-hidden">
        {/* Header */}
        <header className="h-16 border-b border-slate-800 flex items-center justify-between px-8 bg-[#0F172A]/80 backdrop-blur-md z-10">
          <div>
            <h2 className="text-xl font-semibold text-slate-100">Prompt Impact Calculator</h2>
            <p className="text-xs text-slate-400">Real-time telemetry for AI request emissions</p>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 text-xs">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span className="text-slate-400 font-mono">SYSTEM.ONLINE</span>
            </div>
          </div>
        </header>

        {/* Scrollable content */}
        <div className="flex-1 overflow-auto p-8">
          <div className="max-w-6xl mx-auto space-y-8">
            {/* Input Section */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              <div className="lg:col-span-2 space-y-2">
                <div className="flex justify-between items-end">
                  <label className="text-sm font-medium text-slate-300 flex items-center gap-2">
                    <Activity className="h-4 w-4 text-cyan-500" />
                    Input Payload
                  </label>
                  <span className="text-xs text-slate-500 font-mono">{prompt.length} chars</span>
                </div>
                <textarea
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                  className="w-full h-40 bg-slate-900/50 border border-slate-700 focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 rounded-lg p-4 text-sm text-slate-200 font-mono resize-none shadow-inner"
                  placeholder="Enter your AI prompt sequence here..."
                />
              </div>

              <div className="space-y-4">
                <div className="space-y-2">
                  <label className="text-sm font-medium text-slate-300">Target Model</label>
                  <div className="relative">
                    <select className="w-full appearance-none bg-slate-900/50 border border-slate-700 rounded-lg text-sm py-2.5 pl-3 pr-8 text-slate-300 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500">
                      {models.map((m) => (
                        <option key={m}>{m}</option>
                      ))}
                    </select>
                    <ChevronDown className="absolute right-3 top-3 h-4 w-4 text-slate-500 pointer-events-none" />
                  </div>
                </div>

                <div className="space-y-2">
                  <label className="text-sm font-medium text-slate-300">Compute Region</label>
                  <div className="relative">
                    <select className="w-full appearance-none bg-slate-900/50 border border-slate-700 rounded-lg text-sm py-2.5 pl-3 pr-8 text-slate-300 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500">
                      {regions.map((r) => (
                        <option key={r}>{r}</option>
                      ))}
                    </select>
                    <ChevronDown className="absolute right-3 top-3 h-4 w-4 text-slate-500 pointer-events-none" />
                  </div>
                </div>

                <label className="flex items-center gap-3 p-3 bg-slate-900/30 border border-slate-800 rounded-lg cursor-pointer hover:bg-slate-800/50 transition-colors">
                  <input type="checkbox" defaultChecked className="accent-cyan-500 h-4 w-4 rounded bg-slate-900 border-slate-700" />
                  <span className="text-sm text-slate-300">Include response estimate</span>
                </label>
              </div>
            </div>

            <button 
              onClick={() => setIsCalculated(true)}
              className="w-full relative group overflow-hidden rounded-lg bg-blue-600 px-4 py-3 text-sm font-semibold text-white shadow-[0_0_20px_rgba(37,99,235,0.3)] hover:shadow-[0_0_25px_rgba(37,99,235,0.5)] transition-all duration-300"
            >
              <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-cyan-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              <span className="relative flex items-center justify-center gap-2">
                <Zap className="h-4 w-4" />
                Execute Impact Analysis
              </span>
            </button>

            {isCalculated && (
              <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
                {/* Divider */}
                <div className="flex items-center gap-4">
                  <div className="h-[1px] flex-1 bg-slate-800"></div>
                  <span className="text-xs font-mono text-cyan-500 tracking-widest uppercase">Analysis Results</span>
                  <div className="h-[1px] flex-1 bg-slate-800"></div>
                </div>

                {/* Metrics Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                  {/* Total Tokens */}
                  <div className="bg-[#1E293B] border border-slate-700/50 rounded-xl p-5 relative overflow-hidden group hover:border-blue-500/50 transition-colors">
                    <div className="absolute top-0 left-0 w-1 h-full bg-blue-500" />
                    <div className="flex justify-between items-start mb-4">
                      <div className="p-2 bg-slate-900/50 rounded-md border border-slate-700">
                        <Database className="h-4 w-4 text-blue-400" />
                      </div>
                      <span className="text-[10px] font-mono text-slate-500">VOL.1A</span>
                    </div>
                    <p className="text-sm text-slate-400 font-medium mb-1">Total Tokens</p>
                    <div className="flex items-baseline gap-2">
                      <p className="text-3xl font-mono text-slate-100">1,248</p>
                    </div>
                    <div className="mt-3 text-xs text-slate-500 font-mono bg-slate-900/40 py-1 px-2 rounded inline-block">
                      <span className="text-slate-300">248</span> prompt + <span className="text-slate-300">1,000</span> resp
                    </div>
                  </div>

                  {/* Energy Used */}
                  <div className="bg-[#1E293B] border border-slate-700/50 rounded-xl p-5 relative overflow-hidden group hover:border-yellow-500/50 transition-colors">
                    <div className="absolute top-0 left-0 w-1 h-full bg-yellow-500" />
                    <div className="flex justify-between items-start mb-4">
                      <div className="p-2 bg-slate-900/50 rounded-md border border-slate-700">
                        <Battery className="h-4 w-4 text-yellow-400" />
                      </div>
                      <span className="text-[10px] font-mono text-slate-500">PWR.REQ</span>
                    </div>
                    <p className="text-sm text-slate-400 font-medium mb-1">Energy Used</p>
                    <div className="flex items-baseline gap-2">
                      <p className="text-3xl font-mono text-slate-100">0.0145<span className="text-lg text-slate-500 ml-1">Wh</span></p>
                    </div>
                    <div className="mt-3 text-xs text-slate-500 font-mono flex items-center gap-1">
                      <Flame className="h-3 w-3 text-yellow-500/70" />
                      0.0000145 kWh
                    </div>
                  </div>

                  {/* CO2 Emitted */}
                  <div className="bg-[#1E293B] border border-slate-700/50 rounded-xl p-5 relative overflow-hidden group hover:border-rose-500/50 transition-colors">
                    <div className="absolute top-0 left-0 w-1 h-full bg-rose-500" />
                    <div className="flex justify-between items-start mb-4">
                      <div className="p-2 bg-slate-900/50 rounded-md border border-slate-700">
                        <CloudLightning className="h-4 w-4 text-rose-400" />
                      </div>
                      <span className="text-[10px] font-mono text-slate-500">EMS.OUT</span>
                    </div>
                    <p className="text-sm text-slate-400 font-medium mb-1">CO2 Emitted</p>
                    <div className="flex items-baseline gap-2">
                      <p className="text-3xl font-mono text-slate-100">0.0062<span className="text-lg text-slate-500 ml-1">g</span></p>
                    </div>
                    <div className="mt-3 text-xs text-slate-500 font-mono">
                      0.0000062 kg
                    </div>
                  </div>

                  {/* Efficiency Rating */}
                  <div className="bg-[#1E293B] border border-emerald-900/30 rounded-xl p-5 relative overflow-hidden group hover:border-emerald-500/50 transition-colors shadow-[inset_0_0_20px_rgba(16,185,129,0.05)]">
                    <div className="absolute top-0 left-0 w-1 h-full bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]" />
                    <div className="flex justify-between items-start mb-4">
                      <div className="p-2 bg-emerald-950/50 rounded-md border border-emerald-900/50">
                        <Activity className="h-4 w-4 text-emerald-400" />
                      </div>
                      <span className="text-[10px] font-mono text-emerald-500/70">RTG.SYS</span>
                    </div>
                    <p className="text-sm text-slate-400 font-medium mb-1">Efficiency Rating</p>
                    <div className="flex items-baseline gap-2">
                      <p className="text-3xl font-mono font-bold text-emerald-400 drop-shadow-[0_0_8px_rgba(16,185,129,0.4)]">A-</p>
                    </div>
                    <div className="mt-3 text-xs text-emerald-500/70 font-mono uppercase tracking-wider">
                      Optimal Range
                    </div>
                  </div>
                </div>

                {/* Equivalencies Section */}
                <div>
                  <h3 className="text-sm font-semibold text-slate-300 mb-4 flex items-center gap-2">
                    <Globe className="h-4 w-4 text-slate-500" />
                    Environmental Equivalencies
                  </h3>
                  
                  <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
                    {[
                      { label: "Trees", value: "0.0001", unit: "trees/yr", icon: Trees, color: "text-emerald-400", bg: "bg-emerald-400/10", border: "border-emerald-500/20" },
                      { label: "Driving", value: "0.0245", unit: "km", icon: Car, color: "text-slate-300", bg: "bg-slate-800", border: "border-slate-700" },
                      { label: "Charging", value: "0.76", unit: "phones", icon: Smartphone, color: "text-blue-400", bg: "bg-blue-400/10", border: "border-blue-500/20" },
                      { label: "Streaming", value: "0.12", unit: "hrs HD", icon: MonitorPlay, color: "text-indigo-400", bg: "bg-indigo-400/10", border: "border-indigo-500/20" },
                      { label: "Coffee", value: "0.03", unit: "cups", icon: Coffee, color: "text-amber-400", bg: "bg-amber-400/10", border: "border-amber-500/20" },
                    ].map((eq, i) => (
                      <div key={i} className={`flex flex-col items-center justify-center p-4 rounded-lg border ${eq.border} bg-[#1E293B] shadow-sm`}>
                        <div className={`p-2 rounded-full ${eq.bg} mb-3`}>
                          <eq.icon className={`h-5 w-5 ${eq.color}`} />
                        </div>
                        <p className="text-xs text-slate-400 uppercase tracking-wider mb-1 font-semibold">{eq.label}</p>
                        <div className="flex items-baseline gap-1">
                          <span className="text-lg font-mono text-slate-200">{eq.value}</span>
                        </div>
                        <span className="text-[10px] text-slate-500 mt-1">{eq.unit}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Explainer Button */}
                <div className="flex justify-center pt-4">
                  <button className="text-xs font-mono text-slate-400 border border-slate-700 hover:border-slate-500 hover:text-slate-200 bg-slate-900/50 px-4 py-2 rounded flex items-center gap-2 transition-colors">
                    <Info className="h-3 w-3" />
                    [ VIEW RAW LLM TELEMETRY LOGS ]
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
