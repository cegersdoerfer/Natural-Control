function SolChart() {
	return (
		<div className="bg-white bg-opacity-[0.04] flex-col h-[410px] w-[801px] flex items-start px-6 pt-4 pb-6 rounded-2xl border border-white border-opacity-[0.08]">
			<div className="w-full flex-col flex items-start gap-4 font-Inter">
				<div className="w-full flex items-center gap-2 text-sm text-white">
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>1H</div>
					</div>
					<div className="bg-white bg-opacity-[0.08] w-8 h-8 flex justify-center items-center gap-2 p-2 rounded border border-white border-opacity-[0.08] font-semibold">
						<div>1D</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>1M</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>3M</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>1Y</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>2Y</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>3Y</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>5Y</div>
					</div>
					<div className="flex-col h-8 w-8 flex justify-center items-center gap-2 p-2 rounded font-medium">
						<div>ALL</div>
					</div>
				</div>
				<img src="/images/SolChart/Line-2.svg" alt="Line 2" className="h-2.5 w-[753px]" />
				<div className="flex-col flex items-start gap-1">
					<div className="text-5xl leading-[48px] font-semibold text-white">$24.50</div>
					<div className="flex-col flex items-start">
						<div className="text-base font-medium text-[#14f195]">↗$0.74 (3.10%)</div>
						<div className="text-xs text-white">Last update: 3:03 AM, January 27, 2023</div>
					</div>
				</div>
			</div>
			<img src="/images/SolChart/Vector.svg" alt="Vector" className="h-[182px] w-[753px]" />
			<div className="w-full flex justify-end items-center gap-3">
				<img src="/images/SolChart/Frame-626406.svg" alt="Frame 626406" className="h-8 w-8" />
				<img src="/images/SolChart/Frame-626407.svg" alt="Frame 626407" className="h-8 w-8" />
				<img src="/images/SolChart/Frame-626411.svg" alt="Frame 626411" className="h-8 w-8" />
				<img src="/images/SolChart/Frame-626409.svg" alt="Frame 626409" className="h-8 w-8" />
				<img src="/images/SolChart/Frame-626408.svg" alt="Frame 626408" className="h-8 w-8" />
				<img src="/images/SolChart/Frame-626410.svg" alt="Frame 626410" className="h-8 w-8" />
			</div>
		</div>
	);
}
export default SolChart;
