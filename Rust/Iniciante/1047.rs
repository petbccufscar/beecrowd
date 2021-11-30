use std::io;
use std::error::Error;
use std::cmp::Ordering;
use std::ops::Add;
use std::ops::Sub;

#[derive(Eq, PartialEq, PartialOrd)]
struct Momento {
	hora: i64,
	minuto: i64,
}

impl Ord for Momento {
	fn cmp(&self, other: &Self) -> Ordering {
		if self.hora == other.hora {
			return self.minuto.cmp(&other.minuto)
		} else {
			return self.hora.cmp(&other.hora)
		}
	}
}

impl Add for Momento {
	type Output = Self;

	fn add(self, other: Self) -> Self {
		let mut hora = self.hora + other.hora;
		let mut minuto = self.minuto + other.minuto;

		hora += minuto / 60;
		hora %= 24;
		minuto %= 60;

		Self {
			hora: hora,
			minuto: minuto,
		}
	}
}

impl Sub for Momento {
	type Output = Self;

	fn sub(self, other: Self) -> Self::Output {
		let mut hora = self.hora - other.hora;
		let mut minuto = self.minuto - other.minuto;

		if minuto < 0 {
			minuto += 60;
			hora -= 1;
		}

		if hora < 0 {
			hora += 24;
		}

		Self {
			hora: hora,
			minuto: minuto,
		}
	}
}

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let hi: i64 = tokens.next().unwrap().parse()?;
	let mi: i64 = tokens.next().unwrap().parse()?;
	let hf: i64 = tokens.next().unwrap().parse()?;
	let mf: i64 = tokens.next().unwrap().parse()?;

	let inicio = Momento {
		hora: hi,
		minuto: mi,
	};

	let fim = Momento {
		hora: hf,
		minuto: mf,
	};

	let duracao: Momento;

	if inicio == fim {
		duracao = Momento {
			hora: 24,
			minuto: 0,
		}
	} else {
		duracao = fim - inicio;
	}

	println!("O JOGO DUROU {} HORA(S) E {} MINUTO(S)", duracao.hora, duracao.minuto);

	Ok(())
}