// JavaScript: Pelestarian Budaya Papua - TBO (FSA & PDA) Validator
document.addEventListener("DOMContentLoaded", () => {
    // 1. Navigation Scroll Effect & Mobile Menu
    const navbar = document.querySelector(".navbar");
    const menuBtn = document.querySelector(".menu-btn");
    const navLinks = document.querySelector(".nav-links");
    
    window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }

        // Active link detector on scroll
        let current = "";
        const scrollPos = window.scrollY + 120; // offset navbar height plus safety gap
        
        const hero = document.querySelector(".hero");
        if (hero && scrollPos < hero.offsetHeight + hero.offsetTop) {
            current = "";
        } else {
            document.querySelectorAll("section[id]").forEach(section => {
                const top = section.offsetTop;
                const height = section.offsetHeight;
                if (scrollPos >= top && scrollPos < top + height) {
                    current = section.getAttribute("id");
                }
            });
        }
        
        document.querySelectorAll(".nav-link").forEach(link => {
            link.classList.remove("active");
            const href = link.getAttribute("href");
            if (href === "#" && current === "") {
                link.classList.add("active");
            } else if (href === `#${current}`) {
                link.classList.add("active");
            }
        });
    });

    menuBtn.addEventListener("click", () => {
        navLinks.classList.toggle("mobile-active");
    });

    // Close mobile menu on link click
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("mobile-active");
        });
    });

    // 1b. Gallery Category Filter Logic
    const filterBtns = document.querySelectorAll(".filter-btn");
    const galleryItems = document.querySelectorAll(".gallery-item");

    filterBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            filterBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            const filterValue = btn.getAttribute("data-filter");

            galleryItems.forEach(item => {
                const category = item.getAttribute("data-category");
                
                // Add elegant fade transition
                item.style.opacity = "0";
                item.style.transform = "scale(0.95)";
                
                setTimeout(() => {
                    if (filterValue === "all" || category === filterValue) {
                        item.classList.remove("hidden");
                        // Trigger reflow
                        void item.offsetWidth;
                        item.style.opacity = "1";
                        item.style.transform = "scale(1)";
                    } else {
                        item.classList.add("hidden");
                    }
                }, 200);
            });
        });
    });

    // 2. Lexicon & Grammar Rules for Tobati Language
    // Structure: SOV (Subject-Object-Verb) or OSV (Object-Subject-Verb)
    const LEXICON = {
        subjects: {
            "aka": { id: "S", indo: "Saya", type: "Subjek" },
            "iri": { id: "S", indo: "Kamu", type: "Subjek" },
            "ado": { id: "S", indo: "Dia", type: "Subjek" }
        },
        objects: {
            "kai": { id: "O", indo: "ikan", type: "Objek" },
            "ham": { id: "O", indo: "sagu", type: "Objek" },
            "te":  { id: "O", indo: "air", type: "Objek" }
        },
        verbs: {
            "aibi":      { id: "V", indo: "menangkap", type: "Verba" },
            "apri":      { id: "V", indo: "makan", type: "Verba" },
            "ane":       { id: "V", indo: "minum", type: "Verba" },
            "natnahat":  { id: "V", indo: "mengajar", type: "Verba" }
        }
    };

    // Preset examples
    const PRESETS = {
        "preset-1": "aka kai aibi",
        "preset-2": "kai aka aibi",
        "preset-3": "iri ham apri",
        "preset-4": "ado te ane",
        "preset-5": "aka aibi kai", // Invalid (SVO)
        "preset-6": "ham apri",     // Invalid (no Subject)
        "preset-7": "aka kai",      // Invalid (no Verb)
        "preset-8": "iri kai ane"   // Invalid (mismatch: Kamu ikan minum)
    };

    // 3. Tab Navigation for Visualizer
    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            tabBtns.forEach(b => b.classList.remove("active"));
            tabContents.forEach(c => c.classList.remove("active"));
            
            btn.classList.add("active");
            const tabId = btn.getAttribute("data-tab");
            document.getElementById(tabId).classList.add("active");
            
            // Redraw paths if switching to FSA tab
            if (tabId === "fsa-tab") {
                setTimeout(drawFSAPaths, 100);
            }
        });
    });

    // 4. Drawing FSA Transition Arrows dynamically
    const fsaOverlay = document.getElementById("fsa-svg-overlay");
    
    function drawFSAPaths() {
        if (!fsaOverlay) return;
        
        // Clear previous paths
        fsaOverlay.innerHTML = "";
        
        const nodes = {
            q0: document.getElementById("node-q0"),
            q1: document.getElementById("node-q1"),
            q2: document.getElementById("node-q2"),
            q3: document.getElementById("node-q3"),
            q4: document.getElementById("node-q4"),
            q5: document.getElementById("node-q5"),
            q_err: document.getElementById("node-q_err")
        };
        
        const arenaRect = document.querySelector(".fsa-arena").getBoundingClientRect();
        
        const getCenter = (el) => {
            if (!el) return { x: 0, y: 0 };
            const rect = el.getBoundingClientRect();
            return {
                x: (rect.left + rect.right) / 2 - arenaRect.left,
                y: (rect.top + rect.bottom) / 2 - arenaRect.top
            };
        };

        // Transition definitions: [fromNodeId, toNodeId, label, pathId]
        const transitions = [
            { from: "q0", to: "q1", id: "t-q0-q1", text: "Subjek", curve: 0 },
            { from: "q0", to: "q2", id: "t-q0-q2", text: "Objek", curve: 0 },
            { from: "q1", to: "q3", id: "t-q1-q3", text: "Objek", curve: 0 },
            { from: "q2", to: "q4", id: "t-q2-q4", text: "Subjek", curve: 0 },
            { from: "q3", to: "q5", id: "t-q3-q5", text: "Verba", curve: 0 },
            { from: "q4", to: "q5", id: "t-q4-q5", text: "Verba", curve: 0 },
            // Transitions to error state
            { from: "q0", to: "q_err", id: "t-q0-err", text: "Lainnya", curve: -20 },
            { from: "q1", to: "q_err", id: "t-q1-err", text: "Lainnya", curve: -15 },
            { from: "q2", to: "q_err", id: "t-q2-err", text: "Lainnya", curve: -15 },
            { from: "q3", to: "q_err", id: "t-q3-err", text: "Lainnya", curve: -15 },
            { from: "q4", to: "q_err", id: "t-q4-err", text: "Lainnya", curve: -15 },
            { from: "q5", to: "q_err", id: "t-q5-err", text: "Lainnya", curve: 15 }
        ];

        transitions.forEach(trans => {
            const start = getCenter(nodes[trans.from]);
            const end = getCenter(nodes[trans.to]);
            
            if (start.x === 0 || end.x === 0) return; // elements not rendered yet

            // Calculate SVG curve path
            let d = "";
            if (trans.curve === 0) {
                // Straight line
                d = `M ${start.x} ${start.y} L ${end.x} ${end.y}`;
            } else {
                // Curved line using quadratic bezier
                const midX = (start.x + end.x) / 2;
                const midY = (start.y + end.y) / 2 + trans.curve;
                d = `M ${start.x} ${start.y} Q ${midX} ${midY} ${end.x} ${end.y}`;
            }

            // Create path
            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("d", d);
            path.setAttribute("id", trans.id);
            fsaOverlay.appendChild(path);

            // Add marker arrow if supported (using built-in marker or styling)
            path.setAttribute("marker-end", "url(#arrow)");
        });
    }

    // Initialize SVG Arrow marker in DOM
    function initSVGArrowMarker() {
        const svg = document.getElementById("fsa-svg-overlay");
        if (!svg) return;
        const defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
        const marker = document.createElementNS("http://www.w3.org/2000/svg", "marker");
        marker.setAttribute("id", "arrow");
        marker.setAttribute("viewBox", "0 0 10 10");
        marker.setAttribute("refX", "22"); // Offset to avoid overlapping inside the node circle
        marker.setAttribute("refY", "5");
        marker.setAttribute("markerWidth", "6");
        marker.setAttribute("markerHeight", "6");
        marker.setAttribute("orient", "auto-start-reverse");
        
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", "M 0 0 L 10 5 L 0 10 z");
        path.setAttribute("fill", "rgba(255,255,255,0.4)");
        path.setAttribute("id", "arrow-path");
        
        marker.appendChild(path);
        defs.appendChild(marker);
        svg.appendChild(defs);
    }

    initSVGArrowMarker();
    window.addEventListener("resize", drawFSAPaths);
    setTimeout(drawFSAPaths, 200);

    // 5. Simulator Variables and DOM Elements
    const sentenceInput = document.getElementById("sentence-input");
    const btnValidate = document.getElementById("btn-validate");
    const presetTags = document.querySelectorAll(".preset-tag");
    const speedSelect = document.getElementById("speed-select");
    const consoleScreen = document.getElementById("console-screen");
    const btnClearConsole = document.getElementById("clear-console");
    const stackContainer = document.getElementById("stack-container");
    const validationResult = document.getElementById("validation-result");
    const resultTitle = document.getElementById("result-title");
    const resultDesc = document.getElementById("result-desc");
    const resultIcon = document.getElementById("result-icon");
    
    const pdaRules = document.querySelectorAll(".pda-rule-item");

    let isRunning = false;
    let cancelSimulation = false;

    // Helper: Delay function
    const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

    // Console Logging Helper
    function logToConsole(message, type = "info") {
        const line = document.createElement("div");
        line.className = `console-line ${type}`;
        line.innerText = `[${new Date().toLocaleTimeString()}] ${message}`;
        consoleScreen.appendChild(line);
        consoleScreen.scrollTop = consoleScreen.scrollHeight;
    }

    // Set presets event handlers
    presetTags.forEach(tag => {
        tag.addEventListener("click", () => {
            if (isRunning) return;
            presetTags.forEach(t => t.classList.remove("active"));
            tag.classList.add("active");
            const presetId = tag.getAttribute("data-preset");
            sentenceInput.value = PRESETS[presetId];
            logToConsole(`Preset terpilih: "${PRESETS[presetId]}"`, "info");
            resetVisuals();
        });
    });

    btnClearConsole.addEventListener("click", () => {
        consoleScreen.innerHTML = '<div class="console-line info">[Sistem] Konsol siap. Pilih atau ketik kalimat lalu klik Validasi.</div>';
    });

    // Reset simulator UI
    function resetVisuals() {
        // Reset FSA Nodes
        document.querySelectorAll(".fsa-node").forEach(node => {
            node.classList.remove("active", "error-state");
        });
        document.getElementById("node-q0").classList.add("active");

        // Reset FSA Paths
        document.querySelectorAll("#fsa-svg-overlay path").forEach(path => {
            path.className.baseVal = "";
        });

        // Reset PDA Stack
        stackContainer.innerHTML = '<div class="stack-bottom-marker" id="stack-z0">Z₀ (Bottom Marker)</div>';

        // Reset PDA Rule highlights
        pdaRules.forEach(rule => rule.classList.remove("active"));

        // Hide result panel
        validationResult.className = "validation-result-panel";
    }

    // Push token to stack visualizer
    function pushToStack(symbol, label) {
        const item = document.createElement("div");
        item.className = "stack-item";
        item.innerHTML = `
            <span class="stack-item-symbol">${symbol}</span>
            <span class="stack-item-desc">${label}</span>
        `;
        // Insert above stack bottom marker or prior stack items
        const bottom = document.getElementById("stack-z0");
        stackContainer.insertBefore(item, stackContainer.firstChild);
    }

    // Pop token from stack visualizer
    async function popFromStack() {
        const topItem = stackContainer.firstChild;
        if (topItem && topItem.id !== "stack-z0") {
            topItem.classList.add("popping");
            await sleep(300);
            stackContainer.removeChild(topItem);
            return true;
        }
        return false;
    }

    // Perform validation
    btnValidate.addEventListener("click", async () => {
        if (isRunning) {
            // Cancel current execution
            cancelSimulation = true;
            btnValidate.innerText = "Mulai Validasi";
            btnValidate.style.background = "";
            isRunning = false;
            logToConsole("Simulasi dibatalkan oleh pengguna.", "warn");
            return;
        }

        const rawText = sentenceInput.value.trim();
        if (!rawText) {
            logToConsole("Input kosong! Masukkan kalimat untuk divalidasi.", "warn");
            return;
        }

        // Setup running state
        isRunning = true;
        cancelSimulation = false;
        btnValidate.innerText = "Batalkan";
        btnValidate.style.background = "var(--highlight-red)";
        
        resetVisuals();
        logToConsole(`Memulai tokenisasi dan validasi kalimat: "${rawText}"`, "info");

        // Get delay based on speed
        const getDelay = () => parseInt(speedSelect.value);

        // 1. Tokenization
        const tokens = rawText.toLowerCase().split(/\s+/);
        logToConsole(`Token ditemukan (${tokens.length}): [ ${tokens.join(", ")} ]`, "info");
        
        let currentState = "q0";
        let stack = ["Z0"];
        
        let subjekWord = "";
        let objekWord = "";
        let verbaWord = "";
        
        let isGrammarValid = true;

        await sleep(getDelay());

        // Process token by token
        for (let i = 0; i < tokens.length; i++) {
            if (cancelSimulation) break;

            const token = tokens[i];
            logToConsole(`--------------------------------------`, "info");
            logToConsole(`Memproses token ke-${i+1}: "${token}"`, "info");

            // Look up in Lexicon
            let tokenType = null; // 'S', 'O', 'V', or null
            let wordInfo = null;

            if (LEXICON.subjects[token]) {
                tokenType = "S";
                wordInfo = LEXICON.subjects[token];
                subjekWord = token;
            } else if (LEXICON.objects[token]) {
                tokenType = "O";
                wordInfo = LEXICON.objects[token];
                objekWord = token;
            } else if (LEXICON.verbs[token]) {
                tokenType = "V";
                wordInfo = LEXICON.verbs[token];
                verbaWord = token;
            }

            if (tokenType) {
                logToConsole(`Token "${token}" terdeteksi sebagai ${wordInfo.type.toUpperCase()} (${tokenType})`, "info");
            } else {
                logToConsole(`Token "${token}" tidak dikenali dalam kamus bahasa Tobati!`, "error");
                isGrammarValid = false;
            }

            // A. FSA State Transitions
            const previousState = currentState;
            let pathId = "";
            let transitionLabel = "";

            if (isGrammarValid) {
                if (currentState === "q0") {
                    if (tokenType === "S") {
                        currentState = "q1";
                        pathId = "t-q0-q1";
                        transitionLabel = "Membaca Subjek";
                    } else if (tokenType === "O") {
                        currentState = "q2";
                        pathId = "t-q0-q2";
                        transitionLabel = "Membaca Objek";
                    } else {
                        currentState = "q_err";
                        pathId = "t-q0-err";
                        isGrammarValid = false;
                        transitionLabel = "Input tidak sesuai (Bukan Subjek/Objek)";
                    }
                } else if (currentState === "q1") {
                    if (tokenType === "O") {
                        currentState = "q3";
                        pathId = "t-q1-q3";
                        transitionLabel = "Membaca Objek";
                    } else {
                        currentState = "q_err";
                        pathId = "t-q1-err";
                        isGrammarValid = false;
                        transitionLabel = "Struktur Salah (Harus Objek setelah Subjek)";
                    }
                } else if (currentState === "q2") {
                    if (tokenType === "S") {
                        currentState = "q4";
                        pathId = "t-q2-q4";
                        transitionLabel = "Membaca Subjek";
                    } else {
                        currentState = "q_err";
                        pathId = "t-q2-err";
                        isGrammarValid = false;
                        transitionLabel = "Struktur Salah (Harus Subjek setelah Objek)";
                    }
                } else if (currentState === "q3") {
                    if (tokenType === "V") {
                        currentState = "q5";
                        pathId = "t-q3-q5";
                        transitionLabel = "Membaca Verba";
                    } else {
                        currentState = "q_err";
                        pathId = "t-q3-err";
                        isGrammarValid = false;
                        transitionLabel = "Struktur Salah (Harus Verba di akhir kalimat)";
                    }
                } else if (currentState === "q4") {
                    if (tokenType === "V") {
                        currentState = "q5";
                        pathId = "t-q4-q5";
                        transitionLabel = "Membaca Verba";
                    } else {
                        currentState = "q_err";
                        pathId = "t-q4-err";
                        isGrammarValid = false;
                        transitionLabel = "Struktur Salah (Harus Verba di akhir kalimat)";
                    }
                } else if (currentState === "q5") {
                    // Already in accepting state, but extra tokens exist
                    currentState = "q_err";
                    pathId = "t-q5-err";
                    isGrammarValid = false;
                    transitionLabel = "Kelebihan token setelah Kalimat Lengkap";
                }
            } else {
                currentState = "q_err";
            }

            // Update FSA Node visualization
            document.querySelectorAll(".fsa-node").forEach(node => node.classList.remove("active"));
            
            const activeNode = document.getElementById(`node-${currentState}`);
            if (activeNode) {
                if (currentState === "q_err") {
                    activeNode.classList.add("error-state");
                } else {
                    activeNode.classList.add("active");
                }
            }

            // Update FSA path glow
            if (pathId) {
                const pathEl = document.getElementById(pathId);
                if (pathEl) {
                    pathEl.className.baseVal = currentState === "q_err" ? "error" : "active";
                }
            }

            logToConsole(`FSA: Transisi ${previousState.toUpperCase()} -> ${currentState.toUpperCase()} (${transitionLabel})`, isGrammarValid ? "warn" : "error");

            // B. PDA Stack Simulation
            if (isGrammarValid) {
                pdaRules.forEach(rule => rule.classList.remove("active"));

                if (tokenType === "S") {
                    // Push Subject to Stack
                    stack.push("S");
                    pushToStack("S", "Subjek");
                    document.getElementById("pda-r1").classList.add("active");
                    logToConsole(`PDA: Membaca Subjek -> Push "S" ke dalam Stack. Stack: [${stack.join(", ")}]`, "success");
                } else if (tokenType === "O") {
                    // Push Object to Stack
                    stack.push("O");
                    pushToStack("O", "Objek");
                    document.getElementById("pda-r2").classList.add("active");
                    logToConsole(`PDA: Membaca Objek -> Push "O" ke dalam Stack. Stack: [${stack.join(", ")}]`, "success");
                } else if (tokenType === "V") {
                    // Reading Verb -> We validate structural reduction (Pop operations)
                    logToConsole(`PDA: Membaca Verba -> Memulai proses reduksi tata bahasa (Pop Stack)`, "info");
                    
                    if (currentState === "q5" && previousState === "q3") {
                        // SOV reduction: Stack must contain S, O.
                        // Pop O first, then pop S.
                        document.getElementById("pda-r3").classList.add("active");
                        
                        logToConsole(`PDA: Mendeteksi struktur SOV. Memeriksa stack untuk reduksi...`, "info");
                        await sleep(getDelay() / 2);
                        
                        const poppedObj = await popFromStack();
                        if (poppedObj) {
                            stack.pop();
                            logToConsole(`PDA: Pop "O" (Objek) dari stack.`, "success");
                        }
                        
                        await sleep(getDelay() / 2);
                        const poppedSubj = await popFromStack();
                        if (poppedSubj) {
                            stack.pop();
                            logToConsole(`PDA: Pop "S" (Subjek) dari stack.`, "success");
                        }
                        
                    } else if (currentState === "q5" && previousState === "q4") {
                        // OSV reduction: Stack must contain O, S.
                        // Pop S first, then pop O.
                        document.getElementById("pda-r4").classList.add("active");
                        
                        logToConsole(`PDA: Mendeteksi struktur OSV. Memeriksa stack untuk reduksi...`, "info");
                        await sleep(getDelay() / 2);
                        
                        const poppedSubj = await popFromStack();
                        if (poppedSubj) {
                            stack.pop();
                            logToConsole(`PDA: Pop "S" (Subjek) dari stack.`, "success");
                        }
                        
                        await sleep(getDelay() / 2);
                        const poppedObj = await popFromStack();
                        if (poppedObj) {
                            stack.pop();
                            logToConsole(`PDA: Pop "O" (Objek) dari stack.`, "success");
                        }
                    }
                    
                    logToConsole(`PDA: Proses reduksi selesai. Stack: [${stack.join(", ")}]`, "success");
                }
            } else {
                // Grammar error in PDA
                pdaRules.forEach(rule => rule.classList.remove("active"));
                const errorItem = document.createElement("div");
                errorItem.className = "stack-item";
                errorItem.style.border = "1px solid var(--highlight-red)";
                errorItem.style.color = "var(--highlight-red)";
                errorItem.innerHTML = `<span class="stack-item-symbol">ERR</span><span class="stack-item-desc">Mismatched State</span>`;
                stackContainer.insertBefore(errorItem, stackContainer.firstChild);
                logToConsole(`PDA: Pelanggaran tata bahasa! Stack dibekukan.`, "error");
            }

            await sleep(getDelay());
        }

        // Final Validation Assessment
        if (!cancelSimulation) {
            logToConsole(`======================================`, "info");
            logToConsole(`Analisis selesai. Mengevaluasi status akhir...`, "info");

            const isFinalStateAccepting = (currentState === "q5");
            const isStackEmpty = (stack.length === 1 && stack[0] === "Z0");

            if (isGrammarValid && isFinalStateAccepting && isStackEmpty) {
                // SUCCESS
                logToConsole(`KALIMAT VALID! Berhasil diterima oleh FSA (State q5) dan dikosongkan oleh PDA.`, "success");
                
                // Show success panel
                validationResult.className = "validation-result-panel success";
                resultTitle.innerText = "Valid secara Otomata";
                
                // Construct translation
                const subIndo = LEXICON.subjects[subjekWord].indo;
                const objIndo = LEXICON.objects[objekWord].indo;
                const verbIndo = LEXICON.verbs[verbaWord].indo;
                const pattern = subjekWord === tokens[0] ? "SOV" : "OSV";
                
                resultDesc.innerHTML = `Struktur kalimat terverifikasi sebagai pola <strong>${pattern}</strong>.<br>Arti dalam Bahasa Indonesia: <span>"${subIndo} ${verbIndo} ${objIndo}"</span>.`;
                resultIcon.innerHTML = `
                    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                `;
            } else {
                // FAILURE
                logToConsole(`KALIMAT TIDAK VALID! Kalimat ditolak oleh sistem otomata.`, "error");
                
                validationResult.className = "validation-result-panel error";
                resultTitle.innerText = "Struktur Tidak Valid";
                
                // Formulate suggestion based on error
                let suggestion = "Pastikan kalimat mengikuti pola kata bahasa Tobati: Subjek-Objek-Verba (SOV) atau Objek-Subjek-Verba (OSV).";
                
                if (tokens.length < 3) {
                    suggestion = "Kalimat tidak lengkap. Kalimat bahasa Tobati setidaknya membutuhkan Subjek, Objek, dan Kata Kerja (3 token).";
                } else if (currentState === "q_err" || !isGrammarValid) {
                    // Try to diagnose
                    const hasSubject = tokens.some(t => LEXICON.subjects[t]);
                    const hasObject = tokens.some(t => LEXICON.objects[t]);
                    const hasVerb = tokens.some(t => LEXICON.verbs[t]);
                    
                    if (!hasSubject) {
                        suggestion = "Kalimat Anda kehilangan <strong>Subjek</strong> (seperti: <em>aka, iri, ado</em>).";
                    } else if (!hasObject) {
                        suggestion = "Kalimat Anda kehilangan <strong>Objek</strong> (seperti: <em>kai, ham, te</em>).";
                    } else if (!hasVerb) {
                        suggestion = "Kalimat Anda kehilangan <strong>Verba/Kata Kerja</strong> (seperti: <em>aibi, apri, ane</em>).";
                    } else {
                        // SVO or other ordering issues
                        const lastToken = tokens[tokens.length - 1];
                        const isLastVerb = LEXICON.verbs[lastToken];
                        if (!isLastVerb) {
                            suggestion = "Struktur tata bahasa Tobati mengharuskan <strong>Kata Kerja berada di akhir kalimat</strong>.";
                        } else {
                            suggestion = "Susunan kalimat salah. Gunakan pola SOV (misal: <em>aka kai aibi</em>) atau OSV (misal: <em>kai aka aibi</em>).";
                        }
                    }
                }
                
                resultDesc.innerHTML = suggestion;
                resultIcon.innerHTML = `
                    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
                `;
            }
        }

        // Cleanup running state
        btnValidate.innerText = "Mulai Validasi";
        btnValidate.style.background = "";
        isRunning = false;
    });
});
