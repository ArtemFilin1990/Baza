# 📖 Comprehensive Bearing Selection Guide

> **Main document for bearing selection: GOST/ISO → Equivalent → Brand**

[🏠 Home](../../../README.md) | [👨‍💼 Manager's Guide](training/managers_guide.md) | [📋 Equivalents Tables](analogues/README.md) | [🇷🇺 Русская версия](../../bearings/selection_guide.md)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Step-by-Step Selection Algorithm](#step-by-step-selection-algorithm)
3. [GOST ↔ ISO Correspondence Tables](#gost--iso-correspondence-tables)
4. [Manufacturer Classification by Segments](#manufacturer-classification-by-segments)
5. [Additional Parameters and Designations](#additional-parameters-and-designations)
6. [Practical Selection Examples](#practical-selection-examples)
7. [Decision Matrix](#decision-matrix)

---

## Introduction

This guide is designed for **quick and accurate selection** of rolling bearings when replacing domestic (GOST) bearings with imported (ISO) ones and choosing the optimal manufacturer.

### When to Use This Guide

- ✅ Replacing GOST bearings with imported equivalents
- ✅ Selecting bearings by dimensions (d × D × B)
- ✅ Choosing a manufacturer based on requirements and budget
- ✅ Verifying compatibility and interchangeability

### Guide Structure

1. **Selection Algorithm** - step-by-step instructions
2. **Equivalents Tables** - direct GOST ↔ ISO correspondences
3. **Brand Classification** - manufacturer selection by application
4. **Practical Examples** - analysis of typical situations

---

## Step-by-Step Selection Algorithm

### Step 1: Determine Type and Size by GOST

#### 1.1. Identify Bearing Type

**By load direction:**
- **Radial** - support radial load (perpendicular to axis)
- **Thrust** - support axial load (along axis)
- **Angular contact** - combined load

**By rolling element type:**
- **Ball bearings** (type 0, 6, 7, 8 per GOST) - universal, high speeds
- **Roller bearings** (type 2, 3, 5 per GOST) - high loads, medium speeds
- **Needle bearings** (type 4 per GOST) - compact, high loads in small dimensions

#### 1.2. Decode GOST Designation

**GOST bearing number structure:**
```
[Design] [Type] [Series] [Diameter]
    X       X       X        XX

Example: 6205
  6 - deep groove ball bearing
  2 - light series
  05 - bore diameter 25 mm (05 × 5 = 25)
```

**Bore diameter calculation rule:**
- **Last 2 digits × 5 = bore diameter (d) in mm**
  - 04 → 20 mm
  - 05 → 25 mm
  - 06 → 30 mm
  - 10 → 50 mm
  - 20 → 100 mm

**Exceptions:**
- 00 → 10 mm
- 01 → 12 mm
- 02 → 15 mm
- 03 → 17 mm

📚 **More details:** [GOST Designations](designations/gost.md)

---

### Step 2: Finding ISO Equivalent

#### 2.1. Use Correspondence Tables

To find an equivalent, use **GOST ↔ ISO tables** (see section below or [complete tables](analogues/README.md)).

**Examples:**
- GOST **6205** = ISO **6205** (exact match for deep groove ball bearings)
- GOST **2205** = ISO **NU 205** (cylindrical roller)
- GOST **7205** = ISO **30205** (tapered roller)
- GOST **3632** = ISO **22332EAW33** (spherical roller)

#### 2.2. Verify Key Parameters

When selecting an equivalent, always verify:

| Parameter | GOST | ISO | Note |
|-----------|------|-----|------|
| Bore diameter (d) | Must match | Must match | Core dimension |
| Outer diameter (D) | Must match | Must match | Core dimension |
| Width (B) | Must match | Must match | **Often differs!** |
| Dynamic load rating (Cr) | Check catalog | Check catalog | Must be ≥ required |
| Static load rating (C0r) | Check catalog | Check catalog | Must be ≥ required |
| Limiting speed | Check catalog | Check catalog | Must be ≥ operating speed |

⚠️ **Important:** Not all equivalents have identical dimensions! Always check d, D, and especially **B** (width).

---

### Step 3: Choosing a Manufacturer

#### 3.1. Manufacturer Classification

**Premium Segment** (200-400% of average price):
- **SKF** (Sweden) - global leader
- **FAG/INA** (Germany, Schaeffler Group) - premium quality
- **NSK** (Japan) - high precision

**When to choose:**
- Critical equipment (expensive downtime)
- High speeds or precision requirements
- Extreme conditions

**Middle Segment** (100-150% of budget price):
- **NTN, KOYO, NACHI** (Japan) - optimal quality/price
- **Timken** (USA) - tapered roller bearing specialist
- **IKO** (Japan) - needle bearing specialist

**When to choose:**
- General industrial equipment
- Normal operating conditions
- Best value for money

**Budget Segment** (100% baseline):
- **ZWZ, HRB, LYC** (China) - low price
- **GPZ, VPZ** (Russia) - domestic production

**When to choose:**
- Non-critical equipment
- Low loads and speeds
- Limited budget

#### 3.2. Selection Recommendations

1. **Never skimp on critical components** - downtime costs usually far exceed bearing cost
2. **For serial production** - middle segment is optimal (Japanese manufacturers)
3. **For one-time repair** - budget segment acceptable
4. **For high speeds** - only premium or middle segment
5. **Keep spares** - maintain 1-2 spare bearings for critical equipment

---

### Step 4: Verification and Final Selection

#### 4.1. Technical Verification

**Verify load capacity:**
```
Safety factor = Cr (bearing) / P (equivalent load)
Recommended: ≥ 5 for normal conditions
```

**Verify speed:**
```
Speed margin = nmax (bearing) / n (operating)
Recommended: ≥ 2 for normal conditions
```

#### 4.2. Commercial Verification

- Check availability and delivery time
- Compare prices from 2-3 suppliers
- Verify authenticity (certificates, packaging)
- Check warranty terms

---

## GOST ↔ ISO Correspondence Tables

### Quick Reference: Common Bearings

| GOST | ISO | Type | Notes |
|------|-----|------|-------|
| 6204 | 6204 | Deep groove ball | Exact match |
| 6205 | 6205 | Deep groove ball | Exact match |
| 6206 | 6206 | Deep groove ball | Exact match |
| 2205 | NU 205 | Cylindrical roller | Check width! |
| 2305 | NU 305 | Cylindrical roller | Check width! |
| 7205 | 30205 | Tapered roller | Metric series |
| 7305 | 30305 | Tapered roller | Metric series |
| 3632 | 22332EAW33 | Spherical roller | Different designation system |
| 50205 | NJ 205 | Cylindrical roller with ribs | Check design |

📋 **Complete table:** [Complete Equivalents Table](analogues/complete_analogues_table.md) - 2000+ entries

---

## Manufacturer Classification by Segments

### Premium Tier

**SKF (Sweden)**
- Market position: Global #1
- Specialization: All types, especially high-precision
- Average price: 300-400% of budget
- Service life: 2-3× longer than budget
- When to use: Critical applications, high speeds, precision equipment

**FAG/INA (Schaeffler, Germany)**
- Market position: Premium European brand
- Specialization: FAG (all types), INA (roller bearings)
- Average price: 250-350% of budget
- Service life: 2-3× longer than budget
- When to use: Heavy loads, extreme conditions

**NSK (Japan)**
- Market position: Largest Japanese manufacturer
- Specialization: Precision bearings, automotive
- Average price: 200-300% of budget
- Service life: 2× longer than budget
- When to use: High precision, automotive applications

### Middle Tier

**NTN (Japan)**
- Market position: Major Japanese manufacturer
- Specialization: All types, good value
- Average price: 120-150% of budget
- Service life: As calculated
- When to use: General industrial applications

**KOYO (JTEKT, Japan)**
- Market position: Large Japanese manufacturer
- Specialization: Automotive, industrial
- Average price: 120-150% of budget
- Service life: As calculated
- When to use: General industrial applications

**Timken (USA)**
- Market position: Tapered roller specialist
- Specialization: Tapered roller bearings
- Average price: 150-200% of budget
- Service life: Excellent for tapered rollers
- When to use: Heavy loads, rail applications, mining

### Budget Tier

**Chinese Manufacturers (ZWZ, HRB, LYC)**
- Market position: Low-cost alternative
- Specialization: All types
- Average price: 100% baseline
- Service life: 50-70% of premium
- When to use: Non-critical equipment, limited budget

**Russian Manufacturers (GPZ, VPZ)**
- Market position: Domestic production
- Specialization: GOST standard bearings
- Average price: 80-100% of Chinese
- Service life: 50-70% of premium
- When to use: GOST applications, domestic sourcing preference

---

## Additional Parameters and Designations

### Common Suffixes

**Seals:**
- **2RS** or **2RSR** - Contact rubber seals (both sides)
- **2RZ** - Non-contact rubber shields (both sides)
- **Z** or **ZZ** - Metal shields

**Clearance:**
- **C2** - Smaller than normal clearance
- **C0** or no suffix - Normal clearance
- **C3** - Greater than normal clearance
- **C4** - Much greater than normal clearance

**Cage/Retainer:**
- **M** - Brass cage (machined)
- **J** - Steel cage (pressed)
- **P** - Glass fiber reinforced polyamide cage

**Precision:**
- **P0** or no suffix - Normal precision (ABEC 1)
- **P6** - Higher precision (ABEC 3)
- **P5** - High precision (ABEC 5)
- **P4** - Very high precision (ABEC 7)
- **P2** - Ultra-high precision (ABEC 9)

📚 **Complete suffix guide:** [Manufacturer Suffix Cross-Reference](designations/manufacturer_suffixes_cross_reference.md)

---

## Practical Selection Examples

### Example 1: Electric Motor Bearing Replacement

**Situation:** Bearing failed in electric motor AIR 132M4 (11 kW, 1500 rpm)

**Given:**
- Marking on bearing: `6309`
- Measured dimensions: d=45 mm, D=100 mm, B=25 mm
- Normal conditions (temperature up to +40°C, clean room)
- Radial load (rotor weight): ~200 N

**Solution:**
1. Identify: `6309` = deep groove ball bearing
2. Find equivalent: ISO `6309` (exact match)
3. Select manufacturer: NSK, NTN, or KOYO (middle tier)
4. Verify: Cr = 45.2 kN, safety factor = 45200/200 = 226× ✓
5. **Result:** `6309` NSK - optimal choice

📖 **More examples:** [Practical Examples](practical_examples.md)

---

## Decision Matrix

### Quick Decision Table

| Condition | Recommended Type | Manufacturer Tier | Notes |
|-----------|------------------|-------------------|-------|
| High speed (>3000 rpm) | Ball, angular contact | Premium/Middle | Check limiting speed |
| Heavy load (>10 kN) | Roller, spherical | Middle/Premium | Calculate load rating |
| Compact space | Needle | Middle/Premium | Check shaft hardness |
| Dirty environment | Sealed (2RS/2RZ) | Middle/Premium | Extra protection |
| High temperature (>100°C) | Special materials | Premium | Check specs |
| Budget limited | Ball, standard | Budget | Non-critical only |
| Critical equipment | Any suitable | Premium | High reliability needed |
| General industrial | Ball or roller | Middle | Best value |

---

## Conclusion

Proper bearing selection requires considering multiple factors:
- Load type and magnitude
- Operating speed
- Operating conditions
- Precision requirements
- Size constraints
- Budget

Use this guide as a framework for solving your tasks. For complex cases, contact technical specialists from bearing manufacturers - they provide free selection consultations.

---

**Useful Links:**
- [Complete Equivalents Table](analogues/complete_analogues_table.md)
- [GOST Complete Guide](../gost_comprehensive_guide.md)
- [International Brands](brands/international_brands.md)
- [Practical Examples](practical_examples.md)

---

[🏠 Home](../../../README.md) | [👨‍💼 Manager's Guide](training/managers_guide.md) | [📋 Equivalents Tables](analogues/README.md) | [🇷🇺 Русская версия](../../bearings/selection_guide.md)

---

**Created**: 2025-12-29  
**Language**: English  
**Based on**: Russian original selection_guide.md
