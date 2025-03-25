# 🗯️ verbot

A command-line tool that generates verbal content based on context or keyword prompts. Built for testing, research, and creative purposes.

> ⚠️ **DISCLAIMER**: This tool is intended for testing, research, or creative use cases only. It should not be used to harm, harass, or abuse any individuals. The generated content is for demonstration purposes and does not reflect real opinions or intentions.

## 🎯 Features

- 🎲 Random content generation from predefined templates
- 🎯 Keyword-based customization
- 🌡️ Three intensity levels (light, medium, brutal)
- 🏷️ Category filtering (appearance, intelligence, personality)
- 💾 Export capability to text files
- 🔢 Multiple output generation

## 🚀 Installation

```bash
git clone https://github.com/yourusername/verbot.git
cd verbot
pip install -r requirements.txt
```

## 💻 Usage

Basic usage:
```bash
python verbot.py --target "Kevin" --category personality --intensity light
```

Generate multiple outputs:
```bash
python verbot.py --count 3 --intensity medium
```

Save to file:
```bash
python verbot.py --count 5 --save output.txt
```

### Command Options

- `--target`: Name/keyword to customize output (optional)
- `--category`: Content category [appearance|intelligence|personality]
- `--intensity`: Output intensity [light|medium|brutal]
- `--count`: Number of lines to generate
- `--save`: Save output to specified file

## 🧪 Testing

The tool includes default templates for demonstration. You can customize the content by modifying the JSON files in the `data/` directory:

- `light.json`: Light banter
- `medium.json`: Moderate content
- `brutal.json`: Intense content

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

MIT License - see LICENSE file for details.

## ⚠️ Ethics Statement

This tool is designed for:
- Testing content moderation systems
- Creative writing and satire
- Research purposes
- Educational demonstrations

It should NOT be used for:
- Harassment or cyberbullying
- Causing emotional distress
- Any form of abuse or harm

Users are responsible for ensuring ethical usage of this tool.
