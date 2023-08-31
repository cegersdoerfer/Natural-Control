import React from 'react';



// Knob Class Component
class Knob extends React.Component {
	BASE_CLASS_NAME = 'Knob';
	maxKnobValue = 132;
	typeDashLengths = { 1: 184, 2: 251.5 };
	typeValueOffsets = { 1: 132, 2: 0 };
	typePaths = {
		1: 'M20,76 A 40 40 0 1 1 80 76',
		2: 'M50.01,10 A 40 40 0 1 1 50 10',
	}

	state = {
		active: false,
		value: (this.props.initialValue*264/100)-132 || 0,
		currentY: 0,
	};

	updateValue = (mouseY) => {
		let newValue = this.state.value - (mouseY - this.state.currentY);
		
		if (newValue > this.maxKnobValue) { newValue = this.maxKnobValue; }
		else if (newValue < -this.maxKnobValue) { newValue = -this.maxKnobValue; }
		
		this.setState({value: newValue}, () => { 
			this.props.onUpdate && this.props.onUpdate(this.state.value);
		});
	}

    submitValue = () => {
        const brightnessVal = this.state.value;
        fetch('/brightness', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            brightness: brightnessVal
            })
        })
            .then(response => response.json())
            .then(data => {
            if (data.success == true) {
                console.log('Success:', data);
                }
            })
            .catch(error => {
            console.error('Error:', error);
            });
    }
	
	handleMouseMove = (e) => {
		this.updateValue(e.clientY);
		this.setState({currentY: e.clientY});
	}

	handleMouseUp = (e) => {
		window.removeEventListener('mousemove', this.handleMouseMove);
		window.removeEventListener('mouseup', this.handleMouseUp);
		this.setState({currentY: 0});
        this.submitValue();
	}

	handleMouseDown = (e) => {
		this.setState({currentY: e.clientY});
		window.addEventListener('mousemove', this.handleMouseMove);
		window.addEventListener('mouseup', this.handleMouseUp);
	}
	
	getRotation = (val, type) => {
		return this.typeDashLengths[type] - (184/(this.maxKnobValue * 2))*(val + this.typeValueOffsets[type]);
	}

    getLightState = () => {
        return document.getElementById("lightSwitch").checked
    }

	render = () => {
		const { type, color } = this.props;

		return (
			<div className={`${this.BASE_CLASS_NAME}`}>
				<div
					className={`${this.BASE_CLASS_NAME}__container`}
					onMouseDown={this.handleMouseDown}
				>
					<svg className={`${this.BASE_CLASS_NAME}__svg`} viewBox="0 0 100 100">
						<path
							d={"M20,76 A 40 40 0 1 1 80 76"}
							stroke={"#55595C"}
						/>
						<path
							d={this.typePaths[type]}
							stroke={color || "#21CD92"}
							strokeDasharray={this.typeDashLengths[type]}
							style={{
								strokeDashoffset: this.getRotation(this.state.value, type),
								transition: '0.3s cubic-bezier(0, 0, 0.24, 1)'
							}}
						/>
					</svg>
                    {this.getLightState() && (
                        <div className='overlay' style={{
                            backgroundColor: `rgba(0, 0, 0, ${0.5-((this.state.value + 132) * 0.5/264)})`,
                            transition: 'background-color 0.1s ease'
                        }}/>
                    )}
					<div
						className={`${this.BASE_CLASS_NAME}__dial`} 
						style={{transform: `translate(-50%,-50%) rotate(${this.state.value}deg)`}}
					/>
				</div>	
                <div>
                    <p className='knobVal'>
                        {((this.state.value + 132) * (100 / 264)).toFixed(0)}
                    </p>
                </div>
			</div>	
		);
	}
}


export default Knob;