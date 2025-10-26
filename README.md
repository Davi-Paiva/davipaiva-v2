# davipaiva-v2

Version 2 of my personal website - a complete rebuild after one and a half years of working as a fullstack developer and now in my third year of university.

My first website was a simple curriculum site that served its purpose at the time. Now, with real-world development experience under my belt and deeper understanding gained through university studies, I'm rebuilding from the ground up using modern technologies and industry best practices. Time to put my old website to dust! 💨

**Why these tech choices?**
- **React** because it's become my go-to frontend framework
- **Chakra UI** because their design system is just *chef's kiss* 🤌🏼
- **Vite** for that blazing-fast development experience that makes coding actually fun
- **AWS CDK** as a learning adventure in infrastructure-as-code (because manually clicking through AWS console like I did for my first site was... let's just say "educational" 😬)
- **TypeScript** to keep my code from breaking in mysterious ways at 2 AM

This project is equal parts portfolio showcase and personal learning playground. Let's see how much I've grown! 💪🏼

## Prerequisites

Before running this project, make sure you have the following installed:

- [Node.js](https://nodejs.org/) (version 18 or higher)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Davi-Paiva/davipaiva-v2.git
   cd davipaiva-v2
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

## Development

Start the development server:

```bash
npm run dev
# or
yarn dev
```

## Build

Build the project for production:

```bash
npm run build
# or
yarn build
```


## Project Structure

```
davipaiva-v2/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/         # Page components
│   ├── hooks/         # Custom React hooks
│   ├── utils/         # Utility functions
│   ├── theme/         # Chakra UI theme customization
│   └── assets/        # Static assets
├── cdk/               # AWS CDK infrastructure code
├── public/            # Public static files
└── dist/              # Built files (generated)
```

## 📝 TODO List

- [v] Set up React project with Vite
- [v] Deploy the starting project using CDK
- [ ] Configure Chakra UI theme and components
- [ ] Create main layout components (Header, Footer, Navigation)
- [ ] Add About section
- [ ] Add Projects/Portfolio section
- [ ] Add Experience section
- [ ] Add Contact section
- [ ] Add responsive design for mobile devices

