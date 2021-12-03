use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	
	for i in 0..11 {
		for j in 0..3 {
			let k: f64 = (2 * i) as f64 / 10.0;
			
			println!("I={} J={}", k, (j + 1) as f64 + k);
		}
	}

	Ok(())
}