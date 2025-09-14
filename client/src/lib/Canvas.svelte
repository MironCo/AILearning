<script>
	import { onMount } from "svelte";
	import { number } from "../stores";

	let canvas;
	let context;
	const canvasSize = 28;
	const pixelSize = 10; // Size of each pixel
	let isDrawing = false;

	// Initialize the canvas context
	onMount(() => {
		context = canvas.getContext("2d");
		context.fillStyle = "black";
		context.fillRect(0, 0, canvas.width, canvas.height);
	});

	// Handle mouse events
	function startDrawing(event) {
		isDrawing = true;
		draw(event);
	}

	function stopDrawing() {
		isDrawing = false;
		context.beginPath(); // Reset the path
	}

	async function draw(event) {
		if (!isDrawing) return;

		const rect = canvas.getBoundingClientRect();
		const x = event.clientX - rect.left;
		const y = event.clientY - rect.top;

		// Calculate the pixel position
		const pixelX = Math.floor(x / pixelSize) * pixelSize;
		const pixelY = Math.floor(y / pixelSize) * pixelSize;

		context.fillStyle = context.fillStyle === "white" ? "black" : "white";
		context.fillRect(pixelX, pixelY, pixelSize*2, pixelSize*2);

		await sendDataToBackend();
	}

	const drawCircle = (context, centerX, centerY, radius, pixelSize) => {
		for (let y = -radius; y <= radius; y++) { 
			for (let x = -radius; x <= radius; x++) {
				if (x * x + y * y <= radius * radius) {
					context.fillRect(
						centerX + x * pixelSize,
						centerY + y * pixelSize,
						pixelSize,
						pixelSize,
					);
				}
			}
		}
	};

	async function erase() {
		context = canvas.getContext("2d");
		context.fillStyle = "black";
		context.fillRect(0, 0, canvas.width, canvas.height);
		await sendDataToBackend();
	}

	async function sendDataToBackend() {
		const pixels = [];
		for (let y = 0; y < canvasSize; y++) {
			for (let x = 0; x < canvasSize; x++) {
				const imageData = context.getImageData(
					x * pixelSize,
					y * pixelSize,
					pixelSize,
					pixelSize,
				).data;
				let isBlack = true;
				for (let i = 0; i < imageData.length; i += 4) {
					if (
						imageData[i] !== 0 ||
						imageData[i + 1] !== 0 ||
						imageData[i + 2] !== 0
					) {
						isBlack = false;
						break;
					}
				}
				pixels.push(isBlack ? 0 : 255);
			}
		}

		const response = await fetch("http://127.0.0.1:8000/predict", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ pixels }),
		});

		const result = await response.json();
		console.log(result);
		$number = result;
	}
</script>

<div class="container">
	<canvas
		bind:this={canvas}
		width={canvasSize * pixelSize}
		height={canvasSize * pixelSize}
		on:mousedown={startDrawing}
		on:mouseup={stopDrawing}
		on:mousemove={draw}
	></canvas>
	<button class="erase" on:click={erase}> Erase </button>
</div>

<style>
	canvas {
		border: 1px solid #000;
		cursor: crosshair;
		margin: 10%;
	}
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.erase {
		background-color: lightgray;
	}
</style>
